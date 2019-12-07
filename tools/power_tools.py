# we don't use any magic like Data class.
# it is plain old classic design

# tested on Python 3.6 on Windows

import json
import os
import datetime
import copy

# program types in Robot Mesh
PYTHON_TYPE = 41
BLOCKLY_TYPE = 42


class OptUiState(object):
    def __init__(self, east_open, east_width, south_open, south_height, active_tab_middle, active_tab_east):
        self.east_open = east_open
        self.east_width = east_width
        self.south_open = south_open
        self.south_height = south_height
        self.active_tab_middle = active_tab_middle
        self.active_tab_east = active_tab_east

    @classmethod
    def create(cls, dic):
        return OptUiState(dic['eastOpen'],
                          dic['eastWidth'],
                          dic['southOpen'],
                          dic['southHeight'],
                          dic['activeTabMiddle'],
                          dic['activeTabEast'])


class Options(object):
    def __init__(self, use_py_lint, copy_config_to_code, emscripten_con, debugger_enabled, breakpoints,
                 restrictions_on_copy, download_slot, ui_state):
        self.use_py_lint = use_py_lint
        self.copy_config_to_code = copy_config_to_code
        self.emscripten_con = emscripten_con
        self.debugger_enabled = debugger_enabled
        self.breakpoints = breakpoints
        self.restrictions_on_copy = restrictions_on_copy
        self.download_slot = download_slot
        self.ui_state = ui_state

    @classmethod
    def create(cls, dic):
        return Options(dic['optUsePyLint'],
                       dic['optCopyConfigToCode'],
                       dic['optEmscriptenConnectedMode'],
                       dic['optDebuggerEnabled'],
                       dic['optBreakpoints'],
                       dic['optRestrictionsOnCopy'],
                       dic['optDownloadSlot'],
                       OptUiState.create(dic['optUiState']))


class ProgramDesc(object):
    def __init__(self, id, typeid, name, desc, code_file, date_created, date_modified, next_version,
                 old_code_files, old_descs, featured, options):
        self.id = id
        self.typeid = typeid
        self.name = name
        self.desc = desc
        self.code_file = code_file
        self.date_created = datetime.datetime.strptime(date_created, '%Y-%m-%dT%H:%M:%S.%fZ')
        self.date_modified = datetime.datetime.strptime(date_modified, '%Y-%m-%dT%H:%M:%S.%fZ')
        self.next_version = next_version
        self.old_code_files = old_code_files
        self.old_descs = old_descs
        self.featured = featured
        self.options = options

    @classmethod
    def create(cls, dic):
        return ProgramDesc(dic['id'],
                           dic['projectTypeId'],
                           dic['name'],
                           dic['description'],
                           dic['codeFile'],
                           dic['dateCreatedISO'],
                           dic['dateModifiedISO'],
                           dic['nextVersion'],
                           dic['oldCodeFiles'],
                           dic['oldDescriptions'],
                           dic['featured'],
                           Options.create(dic['options'])
                           )


ROOT = r"c:\users\{0}\Documents\RobotMesh\\".format(os.getlogin())


def print_all_programs():
    all_programs_dic = json.load(open(ROOT + "projects.json"))

    all_programs = {}

    for ids, program_dic in all_programs_dic.items():
        id = int(ids)
        program = ProgramDesc.create(program_dic)
        all_programs[id] = program

    # header row
    print('Id\tName          \tSlot\tdateCreated\tdateModified')
    for id, program in all_programs.items():
        print('{0}\t{1}\t{2}\t{3}\t{4}'.format(
            program.id, program.name, program.options.download_slot.replace('user', '#'),
            program.date_created.strftime('%Y-%m-%d'),
            program.date_modified.strftime('%Y-%m-%d')))


def get_datetime_str(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp).isoformat(sep='T', timespec='milliseconds')


def add_program_to_listing(name, slot, description):
    # TODO: 1) warn and prompt if the slot is in use; 2) config oldVersion;
    all_programs_dic = json.load(open(ROOT + "projects.json"))
    json.dump(all_programs_dic, open(ROOT + 'projects-BAK.json', 'wt')) # backup

    n = len(all_programs_dic) # number of current managed programs, new program will be the (n+1)-th one
    newid = str(n+1)

    #copy configuration from 1st one

    model_program = all_programs_dic["1"]

    new_program = copy.deepcopy(model_program) # need a deep copy so original program won't change

    new_program['id'] = newid
    new_program['projectTypeId'] = BLOCKLY_TYPE
    new_program['description'] = description + '[Added to listing by V5PowerTool]'
    new_program['codeFile'] = name + '.py'
    new_program['dateCreatedISO'] = get_datetime_str(os.path.getctime(ROOT + name + '.py'))
    new_program['dateModifiedISO'] = get_datetime_str(os.path.getmtime(ROOT + name + '.py'))

    new_program['options']['optDownloadSlot'] = 'user' + str(slot)

    all_programs_dic[newid] = new_program

    #write back to file
    json.dump(all_programs_dic, open(ROOT + 'projects.json', 'wt'))


if __name__ == '__main__':
    print_all_programs()
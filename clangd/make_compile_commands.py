import json
import os

if not all(item in os.environ for item in ['CMSSW_BASE', 'CMSSW_RELEASE_BASE']):
    raise Exception("Run cmsenv first")

def appendSlash(string):
    if len(string) > 0 and string[-1]!='/':
        string = string + '/'
    return string


# Append the '/' at the end of paths, if not present
CMSSW_BASE = appendSlash(os.getenv('CMSSW_BASE'))
CMSSW_RELEASE_BASE = appendSlash(os.getenv('CMSSW_RELEASE_BASE'))


# Load the JSON files.
with open(CMSSW_BASE+"compile_commands.json", "r") as f:
    compile_commands_preFix = json.load(f)
with open(CMSSW_RELEASE_BASE+"compile_commands.json", "r") as f:
    compile_commands_release = json.load(f)
    files_release = [item['file'] for item in compile_commands_release]


# Update the compile commands of the release with those of the local base
for entry in compile_commands_preFix:
    file = entry['file']
    if file in files_release:
        pos = files_release.index(file)
        compile_commands_release[pos]['directory'] = entry['directory']
        compile_commands_release[pos]['command'] = entry['command']
    else:
        compile_commands_release.append(
            {'command': entry['command'], 'file': entry['file'], 'directory': entry['directory']}
            )

# Store the new commands into the compile_commands.json
with open(CMSSW_BASE+"compile_commands.json", "w") as f:
    json.dump(compile_commands_release, f, indent=4)


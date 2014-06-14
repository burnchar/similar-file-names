# similar_file_names.py - Tries to find possible duplicate files by name
# (C)Charles N. Burns 2014. New BSD License.
import difflib, os, fnmatch

searchPaths = ['c:\itunes']
fileExtensions = ['*.mp3', '*.m4p']

print ("Searching for similar file names matching " + str(fileExtensions) + " in " + str(searchPaths) + "\n" + "-" * 80)

# Gets the full path of files in paths matching patterns (e.g. .txt)
def getFileList(paths, patterns):
	matches = []
	for path in paths:
		for root, dirnames, filenames in os.walk(path):
			for filename in fnmatch.filter(filenames, '*.mkv'):
				matches.append(os.path.join(root, filename))
	return matches

# Build dictionary with key=simplified (comparable) filename and value = full path
fileDict = {}
for file in getFileList(searchPaths, fileExtensions):
	comparableName = os.path.splitext(os.path.basename(file))[0].lower()
	if comparableName in fileDict:
		print("Probable duplicate:\n" + file + "\n" + fileDict[comparableName] + "\n\n")
	else:
		fileDict[comparableName] = file

# Display similar file paths
comparableNames = fileDict.keys()
completedNames = []
for comparableName in comparableNames:
	completedNames.append(comparableName)
	closeMatches = difflib.get_close_matches(comparableName, comparableNames - completedNames, 42, .87)
	completedNames += closeMatches
	if len(closeMatches) > 1:
		print(fileDict[comparableName] + "\n -- Resembles:")
		for closeMatch in closeMatches:
			print(fileDict[closeMatch])
		print("\n")
print("Press a key to exit", end="")
input()


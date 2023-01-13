import os
from urllib.parse import unquote
import shutil

def rename(self, destination):
        UNKNOWN_DIR = destination
        path = UNKNOWN_DIR
        try:
            currentPath = path
            filesList = os.listdir(currentPath)
            newDir = currentPath
            newDir = os.path.join(currentPath, 'renamed')
            print("Debug", currentPath+"/"+"renamed",
                  os.path.exists(currentPath+"/"+"renamed"))
            if not os.path.exists(currentPath+"/"+"renamed"):
                os.mkdir(newDir)

            for item in filesList:
                try:
                    if os.path.isfile(currentPath+"/"+item) and ".py" not in item:
                        # execute rename operation
                        filteredName = unquote(item.rsplit("@", 1)[-1])
                        shutil.copyfile(os.path.join(
                            currentPath, item), os.path.join(newDir, filteredName))
                        print("done", filteredName)
                    else:
                        print("skipped", item)
                except Exception as e:
                    print("failed for", item)
            print("Rename and copy done.")
            print()
        except Exception as e:
            self.label_4.setText("Error occurred:")

        self.label_4.setText("Rename and copy done.")
class Solution:
    def simplifyPath(self, path: str) -> str:
        #Simplifies the path's slashes and configures it so that it starts with one:
        def slashes_dot(directories):
            new_path = ""
            for i  in directories:
                if i != '' and i != '.':
                    new_path += '/' + i
            if new_path == "":
                new_path = "/"
            return new_path

        #Function that adds the up a level directories correspondingly:
        def up_a_level(path):
            bou = path.split('/')
            path_splitted = []
            for i in bou:
                if i != '' and i != '.':
                    path_splitted.append(i)
            print(path_splitted)
            i = 0
            def puncte(path_splitted):
                ok = True
                while ok:
                    ok = False
                    try:
                        if  path_splitted[0] == "..":
                            ok = True
                            path_splitted.pop(0)
                    except:
                        break
                return path_splitted
            print(path_splitted)
            while i < len(path_splitted):
                if i < 0:
                    i = 0
                try:
                    if path_splitted[i+1] == "..":
                        print(i)
                        print(path_splitted)
                        path_splitted.pop(i+1)
                        path_splitted.pop(i)
                        print(path_splitted)
                        i -= 1
                    else:
                        i += 1
                except:
                    break
            path_splitted = puncte(path_splitted)
            new_path = slashes_dot(path_splitted)
            return new_path
        return up_a_level(path)


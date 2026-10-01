class Solution:

    def simplifyPath(self, path: str) -> str:

        stack = []

        parts = path.split('/')

        print(parts)

        for i in range(len(parts)):

            if parts[i] == '' or parts[i] == '.':
                continue

            elif parts[i] == '..':

                if len(stack) > 0:
                    stack.pop()

            else:
                stack.append(parts[i])

        return '/' + '/'.join(stack)


s = Solution()

print(s.simplifyPath("/home/user/../docs"))
from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:

    if not path:
        raise ValueError('Path error.')

    # Uses stack to keep track of current directory in our path search

    stack = []

    # Considers scenario where path is absolute (we'll need to represent the
    # root directory in the normalized path)

    if path[0] == '/':
        stack.append('/')

    # For all meaningful components in the original path

    for component in (component for component in path.split('/') if component not in ['.', '']):

        if component == '..':

            # If path is relative to some current working directory, allow our
            # normalized path to contain a prefix series of '..' directives;

            if not stack or stack[-1] == '..':
                stack.append(component)
            else:

                if stack[-1] == '/':
                    raise ValueError('Trying to escape the matrix, are we?')

                # Go up one directory

                stack.pop()

        else:

            # Otherwise, traverse into a child directory

            stack.append(component)

    normalized = '/'.join(stack)

    # Covers absolute path scenario where initial '/' is joined with '/'

    return normalized[normalized.startswith('//'):]


# print('"/usr/lib/../bin/gcc"\r\n\t=>', shortest_equivalent_path('/usr/lib/../bin/gcc'))
# print('"scripts//./../scripts/awkscripts/./."\r\n\t=>', shortest_equivalent_path('scripts//./../scripts/awkscripts/./.'))
# print('"/usr/.././usr/.././usr/lib/./././var/foo.bat"\r\n\t=>', shortest_equivalent_path('/usr/.././usr/.././usr/lib/./././var/foo.bat'))
# print('"//////////////////////"\r\n\t=>', shortest_equivalent_path('//////////////////////'))
# print('".."\r\n\t=>', shortest_equivalent_path('..'))
# print('"."\r\n\t=>', shortest_equivalent_path('.'))
# print('"./././././././"\r\n\t=>', shortest_equivalent_path('./././././././'))
# print('"/././././././."\r\n\t=>', shortest_equivalent_path('/././././././.'))
# print('"./../"\r\n\t=>', shortest_equivalent_path('./../'))
# print('"../../local"\r\n\t=>', shortest_equivalent_path('../../local'))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))

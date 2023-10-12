# VSCode Project Structure Plus

> Disclaimer: This is an enhanced version of the [VSCode Project Structure](https://marketplace.visualstudio.com/items?itemName=Austin-Lin.vscode-project-structure) extension developed by [Austin-Lin](https://github.com/l02162010/VSCode-Project-Structure). It includes additional functionalities not present in the original version. Once the original extension incorporates these enhancements, this version will be deprecated in favor of the original.

## Description

VSCode Project Structure is a Visual Studio Code extension that allows you to generate a txt file with the folder structure, file name, and file contents of your project.

## Table of Contents

- Features
- Usage
- Examples
- Requirements
- Extension Settings
- Release Notes
- Contributing
- License

## Features

- Generates a txt file with the folder/file structure tree and full file contents of your project.
- Option to exclude certain files and folders based on patterns found in the `.project_structure_ignore` file and/or in the `.gitignore` file
- Option to only include file content for files and folders based on patterns found in the `.project_structure_filter` file
- Customize the folder where the configuration and output files are located (`docs` by default)

## Usage

- Open the command palette (Ctrl+Shift+P on Windows/Linux, Cmd+Shift+P on macOS).
- Type `Generate Project Structure` and select the desired command:
  - `All files`: Generates `project_structure.txt` containing **Project Structure** and **File Contents** for all files, except those matching the **ignore patterns**,
  - `Filtered files`: Also generates `project_structure_filtered.txt` containing both the the **Project Structure** for all files (except those matching the **ignore patterns**), and **File Contents** only for those matching the **filter patterns**
- Wait for the extension to finish generating the file.
- Use `.project_structure_ignore` to list your **ignore patterns**,
- Use `.project_structure_filter` to list your **filter patterns**
- Lines starting with `#` will be ignored in the `.project_structure_ignore` and `.project_structure_filter` files

By default:

- **Ignore patterns** inlude the ones defined in your `.gitignore` file
- All configuration and output files are located in the `docs` directory

Both of the options can be changed in the extension settings.

## Examples

This `.project_structure_ignore` file will cause Project Structure Plus to ignore: the 'node_modules' directory, 'src/entities/index.js' file and any files with the '.log' extension:

```
node_modules
src/entities/index.js
*.log
```

This `.project_structure_filter` file will cause Project Structure to only provide full content of the 'package.json' file, as well as any files in the 'src/entities' folder and subfolders (excluding 'src/entities/index.js' which matches the ignore pattern). _Note that both '\\' and '/' are accepted._

```
src\entities
package.json
```

## Requirements

Visual Studio Code version 1.76.0 or higher.

## Extension Settings

To change extension settings, open your Visual Studio Code settings (File > Preferences > Settings), and search for "Project Structure". You can then:

- Exclude `.gitignore` from the **ignore patterns** (true by default)
- Change the configuration/output folder (`docs` by default).

## Release Notes

- 0.1.5
  - Ignore and filter patterns can include (all or part of) relative paths, including (all or part of) file names and folder names.
  - Accepted path delimiters include "/", "\\" and "\\\\" (to make it compatible with Windows, Linux and Mac)
- 0.1.4
  - lines starting with `#` will be ignored in the `.project_structure_ignore` and `.project_structure_filter` files
- 0.1.3
  - Added option to change the configuration/output folder
  - Added option to apply filter to output file
- 0.0.1
  - Initial release of VSCode Project Structure.

## Contributing

Contributions are always welcome! If you have any ideas or suggestions for new features, feel free to open an issue or a pull request.

## License

This extension is licensed under the MIT License.

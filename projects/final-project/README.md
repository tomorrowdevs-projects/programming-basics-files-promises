# File-Based Task Manager

### Description
Create a file-based task manager application that allows users to manage their tasks and to-do lists.   
Instead of using a traditional database, the application will use text files to store and retrieve task data.

### Features

**Task Creation and Management** 📌
- Users can create new tasks by providing a task name, description, priority, and due date.
- Tasks can be categorized into different lists or projects.
- Users can mark tasks as completed or delete them.

**File Storage and Format** 📁
- Each task will be represented as a structured entry within a text file.
- The application will create and manage separate text files for different projects or lists.
- Each entry in the file will store task attributes such as name, description, priority, due date, and completion status.

**User Interface** 👨‍💻
- Develop a console-based or graphical user interface (GUI) to interact with the task manager.
- Console UI: Use text-based menus and prompts to allow users to input commands and manage tasks.
- GUI: Create a simple graphical interface using a library.

**File I/O Operations** 📃
- Implement functions to read and write task data to text files.
- When the application starts, it should load task data from existing files.
- When tasks are added, modified, or deleted, the corresponding files should be updated.

**Task Filtering and Sorting** 🔃
- Allow users to filter tasks by priority, due date, completion status, or project.
- Implement sorting options to arrange tasks based on different criteria.

**Data Validation** 🔍
- Validate user input to ensure that tasks are created with appropriate information.
- Handle errors gracefully, such as invalid dates or empty task names.

**Backup and Restore (Optional)** 🗄️
- Provide an option to create backups of task data to avoid data loss.
- Allow users to restore task data from a backup file if needed.

**Export and Import (Optional)**
- Add the ability to export task data to a common format (e.g., CSV) for external use.
- Implement importing tasks from an exported file.

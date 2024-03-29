document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('deleteProjectButton').addEventListener('click', function() {
        if (confirm('Are you sure you want to delete this project?')) {
            document.getElementById('deleteProjectForm').submit();
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('deleteTaskButton').addEventListener('click', function() {
        if (confirm('Are you sure you want to delete this task?')) {
            document.getElementById('deleteTaskForm').submit();
        }
    });
});
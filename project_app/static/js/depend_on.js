
        function DependOnField() {
            var parentTask = document.getElementById('parent_task');
            var dependOn = document.getElementById('depend_on');


            if (parentTask.value !== '') {
                dependOn.style.display = 'none';
            } else {
                dependOn.style.display = 'block';
            }
        }

        function handleDependOn() {
            var parentTask = document.getElementById('parent_task');
            var dependOn = document.getElementById('depend_on');

            if (dependOn.value !== '') {
                parentTask.disabled = true;
            } else {
                parentTask.disabled = false;
            }
        }

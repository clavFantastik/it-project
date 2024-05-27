    let clicker = 0;
    edit.addEventListener('click', (e) => {
         e.preventDefault();
         clicker += 1;
         success.classList.toggle('hidden');
         login.classList.toggle('opacity-60');
         email.classList.toggle('opacity-60');
         login.toggleAttribute('disabled');
         email.toggleAttribute('disabled');

         if (clicker % 2 != 0){
             edit.innerHTML = 'Отмена';
             edit.classList.remove('bg-indigo-600');
             edit.classList.add('bg-gray-600');

         }else {
             edit.innerHTML = 'Редактировать';
             edit.classList.remove('bg-gray-600');
             edit.classList.add('bg-indigo-600');
         }
    });
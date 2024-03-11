let tg = window.Telegram.WebApp;

function generateRandomId() {
    const Day = new Date();
    return Math.floor(Math.random() * (999999 - 1 + 1)) + 1 + "#" + Day.getDate()+"-"+("0" + (Day.getMonth() + 1)).slice(-2)+"-"+Day.getFullYear();
}



window.addEventListener('load', function() {
    tg.expand();
    document.getElementById('Name').value = tg.initDataUnsafe.user.first_name + ' ' + tg.initDataUnsafe.user.last_name
    console.log('Страница полностью загружена');
});


function uploadServer(){
    if (typeof tg.initDataUnsafe.user !== 'undefined2'){
        var input = document.getElementById('input_photo')
        var file = input.files[0];
        var orgInput = document.getElementById('org')
        var nameInput = document.getElementById('Name')
        var telInput = document.getElementById('phoneNumber')
        var problemInput = document.getElementById('problem')


        // Проверка наличия данных в полях
        if (!nameInput.value || !orgInput.value || !telInput.value || !problemInput.value) {
            alert('Пожалуйста, заполните все поля формы.'+nameInput.value+ ' ' +orgInput.value+ ' ' +telInput.value+ ' ' +problemInput.value);
            return;
        }


        var formData = new FormData();
        var id = generateRandomId()
        formData.append('id', id);
        formData.append('image', file);
        formData.append('name', nameInput.value);
        formData.append('org', orgInput.value);
        formData.append('phone', telInput.value);
        formData.append('problem', problemInput.value);
        formData.append('Chat_id', tg.initDataUnsafe.user.id);

        var xhr = new XMLHttpRequest();
        xhr.open('POST', 'https://ca57-176-196-232-234.ngrok-free.app/upload', true);
        
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4) {
                if (xhr.status == 200) {
                    var responseData = JSON.parse(xhr.responseText);
                    alert('Заявка отправлена: ' + id);
                    console.log(xhr.responseText);
                    tg.close();
                } else {
                    alert('Ошибка отправки!');
                    console.log(xhr.responseText);
                }
            }
        };

        xhr.send(formData);
    }
    else{
        alert('Отправка разрешина только c Telegram!');
        return;
    }
}
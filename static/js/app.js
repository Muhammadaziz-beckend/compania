const menu_burger = document.querySelector('.burger_menu')
const ul_model = document.querySelector('.model_none')

menu_burger.addEventListener('click', () => {
    ul_model.classList.toggle('none')
}
)


const option = document.querySelector('.select-model')


if (option) {
    option.addEventListener('change', () => {
        let select_ul = option.value

        if (select_ul) {
            location.href = select_ul
        }
    })
}



const form = document.querySelector('.form-input')
const exit = document.querySelector('.exit')
const body = document.querySelector('body')
const foggel_form = document.querySelector('.foggel-form')

foggel_form.addEventListener('click', () => {
    form.classList.toggle('form-none')
    body.classList.toggle('over_flov')
})

exit.addEventListener('click', () => {
    form.classList.toggle('form-none')
    body.classList.toggle('over_flov')
})


const delite = document.querySelector('.delite')
const delite_text = document.querySelector('.delite>.form_conteiner>.delite-items')
const delite_button = document.querySelectorAll('.delite-a>button')




for (i = 0; i < delite_button.length; i++) {
    delite_button[i].addEventListener('click', (event) => {
        [id, ...name_user] = event.currentTarget.value.split(' ')

        console.log(id, name_user);
        delite_text.innerHTML = `
        <p>Вы точно хотите удолить  <br>  "<b>${name_user}</b>"</p>
        
        <div class="chois">
        <a href="">Отмена</a>
            <a href="?deliteOk=${id}">Ок</a>
            </div>
            `
        delite.classList.toggle('delite-none')
    })
}


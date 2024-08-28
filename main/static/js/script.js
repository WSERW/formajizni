let navbar = document.querySelector('.navbar')
let toggler = document.querySelector('.navbar__toggler')

toggler.addEventListener('click', function () {
    navbar.classList.toggle('active')
})

let questions = document.querySelectorAll('.faq__item')

questions.forEach(question => {
    question.addEventListener('click', function () {
        this.classList.toggle('active')
    })
});



const form = document.querySelector('#lead_form');
form.addEventListener('submit', function (event) {
    event.preventDefault();

    const formData = new FormData(form);
    const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch(leadFormEndpoint, {
        method: "POST",
        headers: {
            'X-CSRFToken': csrfToken
        },
        body: formData,
    })
        .then(response => response.json())
        .then(data => {
            const messagesDiv = document.getElementById('form-messages');
            messagesDiv.innerHTML = '';

            if (data.success) {
                messagesDiv.innerHTML = '<div class="alert alert-success">' + data.message + '</div>';
                form.reset();  // Сброс формы после успешной отправки
            } else {
                for (let error in data.errors) {
                    messagesDiv.innerHTML += '<div class="alert alert-danger">' + data.errors[error] + '</div>';
                }
            }
        })
        .catch((error) => {
            const messagesDiv = document.getElementById('form-messages');
            messagesDiv.innerHTML = '<div class="alert alert-danger">Произошла ошибка при отправке формы.</div>';
            console.error('Error:', error);
        });
});


const works_slider = new Swiper('.swiper', {
    // Optional parameters
    loop: true,
    slidesPerView: 3,
    spaceBetween: 20,
    // Navigation arrows
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    }

});


const categoriesGrid = document.querySelector('.category__grid')
const categories = document.querySelectorAll('.category__item')
const worksGrid = document.querySelector('.works__modal')
const works = document.querySelectorAll('.work__item')
const breadcrumbs = document.querySelector('.works__breadcrumbs')
const worksSybtitle = document.querySelector('.works__subtitle')

let activeCategory = 0

function openWorks() {
    categoriesGrid.classList.remove('active')
    worksSybtitle.classList.remove('active')
    breadcrumbs.classList.add('active')
    let bcc = breadcrumbs.querySelectorAll('#worksCategories span')
    let bcw = breadcrumbs.querySelectorAll('#worksItems')
    bcw.forEach(tag => {
        tag.style.display = 'none'
    })
    bcc.forEach(tag => {
        if (tag.dataset.category == activeCategory) {
            tag.style.display = 'inline'
        }
        else {
            tag.style.display = 'none'
        }
    })
    works.forEach(work => {
        if (work.dataset.category == activeCategory && !work.classList.contains('active')) {
            work.classList.add('active')
        }
        else {
            work.classList.remove('active')
        }
    })
}


categories.forEach(category => {
    let overlay = category.querySelector('.category__overlay')
    overlay.addEventListener('click', function (e) {
        activeCategory = category.dataset.selfid
        openWorks()
    })
})



const works_details = document.querySelectorAll('.works__detail__item')


works.forEach(work => {
    let btn = work.querySelector('.works__detail_btn')
    btn.addEventListener('click', function (e) {
        breadcrumbs.querySelector('#worksItems').style.display = 'inline'
        let bcw = breadcrumbs.querySelectorAll('#worksItems span')
        bcw.forEach(tag => {
            if (tag.dataset.work == work.dataset.selfid) {
                tag.style.display = 'inline'
            }
            else {
                tag.style.display = 'none'
            }
        })
        works.forEach(work => {
            work.classList.remove('active')
        })
        works_details.forEach(detail => {
            if (detail.dataset.work == work.dataset.selfid && !detail.classList.contains('active')) {
                detail.classList.add('active')
            }
            else {
                detail.classList.remove('active')
            }
        })
    })
})

const worksDetailClose = document.querySelector('.works__detail_close')
worksDetailClose.addEventListener('click', function () {
    breadcrumbs.querySelector('#worksItems').style.display = 'none'
    let bcw = breadcrumbs.querySelectorAll('#worksItems span')
    bcw.forEach(tag => {
        tag.style.display = 'none'
    })
    openWorks()
    works_details.forEach(detail => {
        detail.classList.remove('active')
    })
})

const closeAll = document.querySelector('#worksBase')
closeAll.addEventListener('click', function () {
    breadcrumbs.classList.remove('active')
    categoriesGrid.classList.add('active')
    worksSybtitle.classList.add('active')

    works_details.forEach(detail => {
        detail.classList.remove('active')
    })

    works.forEach(work => {
        work.classList.remove('active')
    })
})

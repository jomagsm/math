let a = document.getElementsByName('a')[0]
let b = document.getElementsByName('b')[0]
let add = document.getElementsByName('add')[0]
let groupButton = document.getElementsByTagName('button')
let subtract = document.getElementsByName('subtract')[0]
let multiply = document.getElementsByName('multiply')[0]
let divide = document.getElementsByName('divide')[0]
let res = document.getElementById('result')

const BASE_URL = 'http://localhost:8000';


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

async function makeRequest(url, method='GET', data=undefined) {
    let opts = {method, headers: {}};

    if (!csrfSafeMethod(method))
        opts.headers['X-CSRFToken'] = getCookie('csrftoken');
    console.log("test")
    if (data) {
        opts.headers['Content-Type'] = 'application/json';
        opts.body = JSON.stringify(data);
    }

    let response = await fetch(url, opts);

    if (response.ok) {  // нормальный ответ
         return await response.json();
    } else {            // ошибка
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}

async function get_click(event) {
    event.preventDefault()
    try {
        console.log(event)
        let data = {"A": a.value, "B": b.value}
        let url = BASE_URL + '/' + event.target.getAttribute("name") + '/';
        let response = await makeRequest(url, 'POST', data)
        console.log(response)
        res.innerHTML = response.result
        res.style.color = 'green'
        console.log(res)
    }
    catch (e) {
        e = await e.response.json()
        response = await e
        res.innerHTML = response.error
        res.style.color = 'red'
    }
}

async function onLoad() {
    for (let i = 0; i < groupButton.length; i++){
        groupButton[i].onclick = get_click
     }
}
window.addEventListener('load', onLoad);

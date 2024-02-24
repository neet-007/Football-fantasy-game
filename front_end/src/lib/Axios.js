import axios from 'axios'

const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();

            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const config = {
    headers: {
      'Accept':'application/json',
      'Content-type':'application/json',
      'X-CSRFToken': getCookie('csrftoken')
    }
}

export async function getCsrfToken(){
    try {
        let res = await axios.get('/api/auth/get-csrftoken')
        console.log(res.data)
        return res.data
    } catch (error) {
        console.log(error)
    }
}
export async function register({email, password, rePassword}){
    try {
        let res = await axios.post('/api/auth/register/', {email, password, re_password:rePassword}, config)
        console.log(res.data)
        return res.data
    } catch (error) {
        console.log(error)
    }
}
export async function login({email, password}){
    try {
        let res = await axios.post('/api/auth/login/', {email, password}, config)
        console.log(res.data)
        return res.data
    } catch (error) {
        console.log(error)
    }
}
export async function logout(){
    try {
        let res = await axios.post('/api/auth/login', {}, config)
        console.log(res.data)
        return res.data
    } catch (error) {
        console.log(error)
    }
}
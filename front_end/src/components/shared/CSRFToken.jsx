import React, {useState, useEffect}from 'react'
import { getCsrfToken } from '../../lib/axios';;

export function CSRFToken(){
    const [csrfToken, setCsrfToken] = useState('')
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

  useEffect(()=>{
    getCsrfToken().then(() => {
        setCsrfToken(getCookie('csrftoken'))
    })
  },[])
  console.log(csrfToken)
  return (
    <input type="hidden" name='csrfmiddlewaretoken'  value={csrfToken} readOnly/>
  )
}

import React, { useRef } from 'react'
import Button from '../../../components/shared/Button/Button'
import {CSRFToken} from '../../../components/shared/CSRFToken'
import { useMainContext } from '../../../context/MainContext'
import { useLogin } from '../../../lib/queriesAndMutaions'

function Login() {
  const {setUser, isAuthenticated, setIsAuthenticated} = useMainContext()
  const {mutateAsync:login} = useLogin()
  const emailRef = useRef()
  const passwordRef = useRef()

  function handleSubmit(e){
    e.preventDefault()
    login({email:emailRef.current.value, password:passwordRef.current.value}).then(res => {
    })
  }
  return (
    <form className='auth-layout_form' onSubmit={handleSubmit}>
        <CSRFToken/>
        <span className='d-flex f-di-column'>
            <label htmlFor='login-email'>email</label>
            <input id='login-email' className='auth-layout_form-input'
            required type='email' ref={emailRef}/>
        </span>
        <span className='d-flex f-di-column'>
            <label htmlFor='login-password'>password</label>
            <input id='login-password' className='auth-layout_form-input'
            required type='password' minLength={8} ref={passwordRef}/>
        </span>
        <Button className={'cap'} childern='' type='submit'>login</Button>
    </form>
  )
}

export default Login
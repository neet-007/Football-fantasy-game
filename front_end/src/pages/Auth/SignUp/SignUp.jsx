import React, { useRef } from 'react'
import Button from '../../../components/shared/Button/Button'
import { CSRFToken } from '../../../components/shared/CSRFToken'
import {useMainContext} from '../../../context/MainContext'
import { useRegister } from '../../../lib/queriesAndMutaions'
import { redirect } from 'react-router-dom'

function SignUp() {
  //const {isAuthenticated} = useMainContext()
  const {mutateAsync:register} = useRegister()
  const emailRef = useRef()
  const passwordRef = useRef()
  const rePasswordRef = useRef()

  function handleSubmit(e){
    e.preventDefault()
    register({email:emailRef.current.value, password:passwordRef.current.value, rePassword:rePasswordRef.current.value}).then(res =>{
      if (res.status !== 201) return console.log(res.error)
      return redirect('./login')
    })
  }
  //if (isAuthenticated) return redirect('')
  return (
    <form className='auth-layout_form' onSubmit={handleSubmit}>
        <CSRFToken/>
        <span className='d-flex f-di-column'>
            <label htmlFor='sign-up-email'>email</label>
            <input id='sign-up-email' className='auth-layout_form-input'
            required type='email' ref={emailRef}/>
        </span>
        <span className='d-flex f-di-column'>
            <label htmlFor='sign-up-password'>password</label>
            <input id='sign-up-password' className='auth-layout_form-input'
            required type='password' minLength={8} ref={passwordRef}/>
        </span>
        <span className='d-flex f-di-column'>
            <label htmlFor='sign-up-re-password'>re password</label>
            <input id='sign-up-re-password' className='auth-layout_form-input'
            required type='password' minLength={8} ref={rePasswordRef}/>
        </span>
        <Button className={'cap'} childern='' type='submit'>sign up</Button>
    </form>
  )
}

export default SignUp
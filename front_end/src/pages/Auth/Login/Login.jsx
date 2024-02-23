import React from 'react'
import Button from '../../../components/shared/Button/Button'

function Login() {
  function handleSubmit(e){
    e.preventDefault()
    console.log('dasd')
  }
  return (
    <form className='auth-layout_form' onSubmit={handleSubmit}>
        <span className='d-flex f-di-column'>
            <label htmlFor='login-email'>email</label>
            <input id='login-email' className='auth-layout_form-input'
            required type='email'/>
        </span>
        <span className='d-flex f-di-column'>
            <label htmlFor='login-password'>password</label>
            <input id='login-password' className='auth-layout_form-input'
            required type='password' minLength={8}/>
        </span>
        <Button className={'cap'} childern='' type='submit'>login</Button>
    </form>
  )
}

export default Login
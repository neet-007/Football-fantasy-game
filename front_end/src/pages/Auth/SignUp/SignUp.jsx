import React from 'react'
import Button from '../../../components/shared/Button/Button'

function SignUp() {

  function handleSubmit(e){
    e.preventDefault()
    console.log('sadasd')
  }
  return (
    <form className='auth-layout_form' onSubmit={handleSubmit}>
        <span className='d-flex f-di-column'>
            <label htmlFor='sign-up-email'>email</label>
            <input id='sign-up-email' className='auth-layout_form-input'
            required type='email'/>
        </span>
        <span className='d-flex f-di-column'>
            <label htmlFor='sign-up-password'>password</label>
            <input id='sign-up-password' className='auth-layout_form-input'
            required type='password' minLength={8}/>
        </span>
        <span className='d-flex f-di-column'>
            <label htmlFor='sign-up-re-password'>re password</label>
            <input id='sign-up-re-password' className='auth-layout_form-input'
            required type='password' minLength={8}/>
        </span>
        <Button className={'cap'} childern='' type='submit'>sign up</Button>
    </form>
  )
}

export default SignUp
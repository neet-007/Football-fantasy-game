import React from 'react'
import {createPortal} from 'react-dom'
import './Modal.css'

function Modal({isOpen, className, children}) {
  if (!isOpen) return null
  return createPortal(
    <>
        <div id='modal-overlay' className='modal_overlay'/>
        <div className={`modal_modal ${className}`}>
            {children}
        </div>
    </>,
    document.getElementById('portal')
  )
}

export default Modal
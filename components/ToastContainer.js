const { h } = require('hyperapp')
import Toast from './Toast.js'

const ToastContainer = module.exports = ({toasts, actions}) => <div className='toast-container'>
    {toasts.map((t) => <Toast text={t} actions={actions} />)}
</div>


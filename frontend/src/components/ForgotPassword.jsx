import React, { useRef, useState } from "react"
import { useAuth } from "../context/AuthContext"
import { Link, useNavigate } from "react-router-dom"
import loginCover from '../sources/loginCover.jpg'

export default function ForgotPassword() {
  const emailRef = useRef()
  const { resetpassword } = useAuth()
  const [error, setError] = useState("")
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate();

  async function handleSubmit(e) {
    e.preventDefault()


    try {
      setError("")
      setLoading(true)
      await resetpassword(emailRef.current.value)
      navigate('/');
    } catch {
      setError("Failed to sign in")
    }

    setLoading(false)
  }

  return (

    <div className='relative w-full h-screen bg-zinc-900/90'>
        <img src='https://media.istockphoto.com/photos/wooden-brown-books-shelves-with-a-lamp-picture-id1085770318' className="absolute w-full h-full object-cover mix-blend-overlay" />
       
        <div className='flex items-center justify-center h-full'>
            <form className='max-w-[400px] w-full mx-auto rounded-lg bg-white p-10'>
                <h2 className='text-4xl font-bold text-center py-5'>Bibliophile's Tool</h2>
                {error && <div role="alert"> <div className="border relative border-red-400 rounded-b bg-red-100 px-4 py-3 text-red-700"> <p>{error}</p> </div> </div>}
                <div className='flex flex-col mb-4'>
                    <label className="border-none relative">Email</label>
                    <input className='rounded-lg border relative  bg-gray-100 p-2' type="text" ref={emailRef} required />
                </div>
                
                <p className="text-center mt-4 border-none relative ">
                    <Link to={"/login"} class="underline"> Log In</Link>
                </p>
                <p className="text-center mt-4 border-none relative ">
                    Need an account? <Link to={"/signup"} class="underline"> Sign up</Link>
                </p>
                <button disabled={loading} onClick={handleSubmit} className='w-full my-5 py-2 border relative bg-teal-500 shadow-lg shadow-teal-500/50 hover:shadow-teal-500/40 text-white font-semibold rounded-lg'>Reset Password</button>
                
            </form>
        </div>
    </div>
  )
}
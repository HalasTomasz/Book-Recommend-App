import React, { useRef, useState } from "react"
import { useAuth } from "../context/AuthContext"
import { Link, useNavigate } from "react-router-dom"


export default function Login() {
  const emailRef = useRef()
  const passwordRef = useRef()
  const {login } = useAuth()
  const [error, setError] = useState("")
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate();

  async function handleSubmit(e) {
    e.preventDefault()


    try {
      setError("")
      setLoading(true)
      await login(emailRef.current.value, passwordRef.current.value)
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
                {error && <div role="alert"> <div className="border relative  border-red-400 rounded-b bg-red-100 px-4 py-3 text-red-700"> <p>{error}</p> </div> </div>}
                <div className='flex flex-col mb-4'>
                    <label className="border-none relative">Email</label>
                    <input className='rounded-lg border relative  bg-gray-100 p-2' type="text" ref={emailRef} required />
                </div>
                <div className='flex flex-col'>
                    <label className="border-none relative">Password</label>
                    <input className='p-2 border relative rounded-lg bg-gray-100  text-whitemt-2 ' type="password" ref={passwordRef} required />
                </div>

                <p className="text-center mt-4 border-none relative ">
                    Need an account? <Link to={"/signup"} className="underline"> Sign up</Link>
                </p>
                <p className="text-center mt-4 border-none relative ">
                    <Link to={"/forgot-password"} className="underline"> Forgot password?</Link>
                </p>
                <button disabled={loading} onClick={handleSubmit} className='w-full my-5 py-2 border relative bg-teal-500 shadow-lg shadow-teal-500/50 hover:shadow-teal-500/40 text-white font-semibold rounded-lg'>SIGN IN</button>
                
            </form>
        </div>
    </div>
  )
}
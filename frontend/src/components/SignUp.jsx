import React, { useRef, useState, useEffect } from "react"
import { useAuth } from "../context/AuthContext"
import {useDispatch, useSelector} from 'react-redux'
import { Link, useNavigate } from "react-router-dom"
import { listGenre } from "../actions/genreAction"
import Select from 'react-tailwindcss-select'

export default function Signup() {
  const emailRef = useRef()
  const passwordRef = useRef()
  const passwordConfirmRef = useRef()
  const userNameRef= useRef()
  const {signup} = useAuth()
  const [errorMess, setError] = useState("")
  const [loadingtype, setLoading] = useState(false)
  const navigate = useNavigate();

  const dispatch = useDispatch()

  const [userAge, setUserAge] = useState(null);  
  const ages = [
    {value: "16", label: "🦊 0-16"},
    {value: "26", label: "🦋 16-26"},
    {value: "40", label: "🐝 26-40"},
    {value: "60", label: "🐝 40-60"},
    {value: "200", label: "🐝 60-∞"},
    {value: "0", label: "🦊 Don't want to say"},
    ];

  const [userSex, setUserSex] = useState(null);  
  const sex = [
    {value: "Man", label: "🦊 Man"},
    {value: "Woman", label: "🦋 Woman"},
    {value: "No", label: "🐝 Don't want to say"},
    ];

    const [userGenre, setUserGenre] = useState(null);  
    
     useEffect(() => {

      dispatch(listGenre())
  
    }, [dispatch])

    const genreData = useSelector(state => state.getGenre.genres)
    const bookGenres = genreData.map(Genre_Name  => { return {value: Genre_Name.Genre_Name, label:Genre_Name.Genre_Name}});
    console.log(bookGenres)

    const handleUserAgeChange = (value) => {
        setUserAge(value);
    };

    const handleUserSexChange = (value) => {
        setUserSex(value);
    };

    const handleUserGenreChange = (value) => {
        setUserGenre(value);
    };

  async function handleSubmit(e) {
    e.preventDefault()
   
    if (passwordRef.current.value !== passwordConfirmRef.current.value) {
      setError("Passwords do not match")
      return
    }

    if (userGenre === null){
      setError("Type book's genre")
      return
    }

    const usertypes = userGenre.map( item => { return item.value })
  
    try {
      setError("")
      setLoading(true)
      await signup(emailRef.current.value, passwordRef.current.value, userNameRef.current.value, userAge['value'], userSex['value'], usertypes)
      navigate('/');
    } catch {
      setError("Failed to create an account")
    }

    setLoading(false)
  }

  return (

    <div className='relative w-full h-screen bg-zinc-900/90'>
        <img src='https://media.istockphoto.com/photos/wooden-brown-books-shelves-with-a-lamp-picture-id1085770318' className="absolute w-full h-full object-cover mix-blend-overlay" />
       
        <div className='flex items-center justify-center h-full'>
            <form className='max-w-[400px] w-full mx-auto rounded-lg bg-white p-10'>
                <h2 className='text-4xl font-bold text-center py-5'>Bibliophile's Tool</h2>
                {errorMess && <div role="alert"> <div className="border relative border-red-400 rounded-b bg-red-100 px-4 py-3 text-red-700"> <p>{errorMess}</p> </div> </div>}
                <div className='flex flex-col pb-2'>
                    <label className="border-none relative">Email</label>
                    <input className='rounded-lg border relative  bg-gray-100 p-2' type="text" ref={emailRef} required />
                </div>
                <div className='flex flex-col pb-2'>
                    <label className="border-none relative">Password</label>
                    <input className='p-2 border relative rounded-lg bg-gray-100  text-whitemt-2 ' type="password" ref={passwordRef} required />
                </div>
                <div className='flex flex-col pb-2'>
                    <label className="border-none relative">Password Confirmation</label>
                    <input className='p-2 border relative rounded-lg bg-gray-100  text-whitemt-2 ' type="password" ref={passwordConfirmRef} required />
                </div>
                <div className='flex flex-col pb-2'>
                    <label className="border-none relative">Username</label>
                    <input className='rounded-lg border relative  bg-gray-100 p-2' type="text" ref={userNameRef} required />
                </div>
                <div className='flex flex-col border-none relative pb-2'>
                    <label htmlFor="age">Age</label>
                    <Select value={userAge} onChange={handleUserAgeChange} options={ages} />
                </div>
                <div className='flex flex-col border-none relative pb-2'>
                    <label htmlFor="gender">Sex</label>
                    <Select value={userSex} onChange={handleUserSexChange} options={sex} />
                </div>
                <div className='flex flex-col mb-4 border-none relative pb-2'>
                    <label htmlFor="genre">Genre I enjoy reading</label>
                    <Select value={userGenre} onChange={handleUserGenreChange} options={bookGenres} isMultiple={true} />
                </div>
               
                
                <p className="text-center mt-10 border-none relative ">
                    Already have an account? <Link to={"/login"} className="underline"> Log In</Link>
                </p>
                <button disabled={loadingtype} onClick={handleSubmit} className='w-full my-5 py-2 border relative bg-teal-500 shadow-lg shadow-teal-500/50 hover:shadow-teal-500/40 text-white font-semibold rounded-lg'>SIGN IN</button>
                
            </form>
        </div>
    </div>
  )
}
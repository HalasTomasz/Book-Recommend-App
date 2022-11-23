import React, { useRef, useState, useEffect} from "react"
import { useAuth } from "../context/AuthContext"
import { Link, useNavigate } from "react-router-dom"
import {getUser, updateUser} from '../actions/userAction'
import {useDispatch, useSelector} from 'react-redux'
import { listGenre,  listUserGenre, updateUserGenre} from "../actions/genreAction"
import Select from 'react-tailwindcss-select'
import { FirebaseError } from "firebase/app"

export default function Profil() {

    const navigate = useNavigate();
    const dispatch = useDispatch();
    const { currentUser, updateemail, updatepassword } = useAuth()
   
    useEffect(() => {
        dispatch(getUser(currentUser.uid))
        dispatch(listGenre())
        dispatch(listUserGenre(currentUser.uid))
      },[dispatch])

    const emailRef = useRef()
    const userNameRef = useRef()
    const passwordRef = useRef()
    const passwordConfirmRef = useRef()
  const userDBData = useSelector(state => state.getUser)
  const {errors, loadings, user} = userDBData
  const userGenreTypes = useSelector(state => state.getUserGenre.user_genres)
  const genreData = useSelector(state => state.getGenre.genres)
  const bookGenres = genreData.map(Genre_Name  => { return {value: Genre_Name.Genre_Name, label:Genre_Name.Genre_Name}});
  const userGenres = userGenreTypes.map(Genre_Name  => { return {value: Genre_Name.Genre_Name, label:Genre_Name.Genre_Name}});
  const [userGenre, setUserGenre] = useState(userGenres);
  const [userSex, setUserSex] = useState({value:user.Sex,label:user.Sex});  
  const [userAge, setUserAge] = useState({value:user.Age, label:user.Age});
  const [name, SetName] = useState(user.Name)
  const [errorMess, setError] = useState("")
  const [loadingtype, setLoading] = useState(false)
  console.log(user)
 
  const ages = [
    {value: "16", label: "🦊 0-16"},
    {value: "26", label: "🦋 16-26"},
    {value: "40", label: "🐝 26-40"},
    {value: "60", label: "🐝 40-60"},
    {value: "200", label: "🐝 60-∞"},
    {value: "0", label: "🦊 Don't want to say"},
    ];

  const sex = [
    {value: "Man", label: "Man"},
    {value: "Woman", label: "Woman"},
    {value: "No", label: "Don't want to say"},
    ];

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
      return setError("Passwords do not match")
    } 

    const promisies = []
    setError("")
    setLoading(true)

    if (emailRef.current.value !== currentUser.email){
        promisies.push(updateemail(emailRef.current.value))
    }

    if (passwordRef.current.value){
       promisies.push(updatepassword(passwordRef.current.value))
    }
 
    if (userSex['value'] !== user.Sex || userNameRef.current.value !== user.Name || userAge['value'] !== user.Age ){
     promisies.push(dispatch(updateUser(userNameRef.current.value, user.FireBaseAuth, userSex['value'], userAge['value'])))
    }
  
    if (userGenres !== userGenre ){
        const usertypes = userGenre.map( item => { return item.value })
        promisies.push(dispatch(updateUserGenre(usertypes,currentUser.uid)))
      }


    Promise.all(promisies).then(() =>{
        SetName(userNameRef.current.value)
        setUserAge(userAge['value'])
        setUserGenre(userGenre)
        setUserSex(userSex['value'])
        navigate('/');
    }).catch((ex) =>{
        if (ex instanceof FirebaseError){
            setError('Login in again to change password or email')
        }
        else{
            setError('Failed to update an account')
        }
    }).finally(() =>{
        setLoading(false)
    })
  }

  return (

   <div className='relative w-full h-screen bg-zinc-900/90'>
        <img src='https://media.istockphoto.com/photos/wooden-brown-books-shelves-with-a-lamp-picture-id1085770318' className="h-full absolute w-full object-cover mix-blend-overlay" />
        <div className='flex items-center justify-center h-auto pt-10 '>
            <form className='max-w-[400px] w-full mx-auto rounded-lg bg-white p-10'>
                <h2 className='text-4xl font-bold text-center py-5'>Update User</h2>
                {errorMess && <div role="alert"> <div className="border relative border-red-400 rounded-b bg-red-100 px-4 py-3 text-red-700"> <p>{errorMess}</p> </div> </div>}
                <div className='flex flex-col pb-2'>
                    <label className="border-none relative">Update Email</label>
                    <input className='rounded-lg border relative  bg-gray-100 p-2' type="text" ref={emailRef} required defaultValue={currentUser.email} />
                </div>
                <div className='flex flex-col pb-2'>
                    <label className="border-none relative">Update Password</label>
                    <input className='p-2 border relative rounded-lg bg-gray-100  text-whitemt-2 ' placeholder="Leave blank to keep the same" type="password" ref={passwordRef} required />
                </div>
                <div className='flex flex-col pb-2'>
                    <label className="border-none relative">Password Confirmation</label>
                    <input className='p-2 border relative rounded-lg bg-gray-100  text-whitemt-2 ' placeholder="Leave blank to keep the same" type="password" ref={passwordConfirmRef} required />
                </div>
                <div className='flex flex-col pb-2'>
                    <label className="border-none relative">Username</label>
                    <input className='rounded-lg border relative  bg-gray-100 p-2' type="text" ref={userNameRef} required  defaultValue={name}/>
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
                    <Select  value={userGenre} onChange={handleUserGenreChange} options={bookGenres} isMultiple={true} />
                </div>
                <button disabled={loadingtype} onClick={handleSubmit} className='w-full my-5 py-2 border relative bg-teal-500 shadow-lg shadow-teal-500/50 hover:shadow-teal-500/40 text-white font-semibold rounded-lg'>Return</button>
                
            </form>
        </div>
    </div>
  )
}
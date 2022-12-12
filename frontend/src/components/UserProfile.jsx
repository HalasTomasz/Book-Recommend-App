import React, { useRef, useState, useEffect} from "react"
import { useAuth } from "../context/AuthContext"
import { Link, useNavigate } from "react-router-dom"
import {getUser, updateUser} from '../actions/userAction'
import {useDispatch, useSelector} from 'react-redux'
import { listGenreShort,  listUserGenre, updateUserGenre} from "../actions/genreAction"
import Select from 'react-select'
import { FirebaseError } from "firebase/app"

export default function Profil() {

    const navigate = useNavigate();
    const dispatch = useDispatch();
    const { currentUser, updateemail, updatepassword } = useAuth()
    const ages_prop = [
        {id:0, value: "16"},
        {id:1, value: "26"},
        {id:2, value: "40"},
        {id:3, value: "60"},
        {id:4, value: "200"},
        {id:5, value: "0"},
        ];
    const ages = [
            {value: "16", label: "0-16"},
            {value: "26", label: "16-26"},
            {value: "40", label: "26-40"},
            {value: "60", label: "40-60"},
            { value: "200", label: "60-∞"},
            { value: "0", label: "Don't want to say"},
            ];
        
      const sex_prop = [
        {id:0, value: "Man", },
        {id:1, value: "Woman"},
        {id:2, value: "No"},
        ];
    const sex = [
            {value: "Man", label: "Man"},
            {value: "Woman", label: "Woman"},
            {value: "No", label: "Don't want to say"},
            ];

    useEffect(() => {
        dispatch(getUser(currentUser.uid))
        dispatch(listGenreShort())
      },[dispatch, currentUser])

    const emailRef = useRef()
    const userNameRef = useRef()
    const passwordRef = useRef()
    const passwordConfirmRef = useRef()
    const userDBData = useSelector(state => state.getUser)
    const {loading, error, user} = userDBData
    //const {loadingGenreTypes, errorGenreTypes, userGenreTypes} = useSelector(state => state.getUserGenre)
    const {loading_genre, error_genre, genres_short} = useSelector(state => state.getShortGenre)
    //console.log(userGenreTypes)
    //console.log(genreData)
    // const userGenres = userGenreTypes.map(Genre_Name  => { return {value: Genre_Name.Genre_Name, label:Genre_Name.Genre_Name}});
    // {!loadinggenreData && const bookGenres = genreData.map(Genre_Name  => { return {value: Genre_Name.Genre_Name, label:Genre_Name.Genre_Name}})}
    const [userGenre, setUserGenre] = useState([]);
    const [userSex, setUserSex] = useState();  
    const [userAge, setUserAge] = useState();
    const [errorMess, setError] = useState("")
    const [loadingtype, setLoading] = useState(false)

    
    //console.log(userGenre)
    //console.log(userSex)
    //console.log(userAge)

    const returnIndexAge = (age) =>{
        const index = ages_prop.filter(x => x.value == age).map(x => x.id)
        return index[0]
    }

    const returnIndexSex = (sex) =>{
        const index = sex_prop.filter(x => x.value == sex).map(x => x.id)
        return index[0]
    }


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
 
    if (userNameRef.current.value !== user.Name || userAge != null || userSex != null ){

        const user_name = userNameRef.current.value !== user.Name ? userNameRef.current.value : user.Name
        const user_age = userAge != null ? userAge['value'] : user.Age
        const user_sex = userSex != null ? userSex['value'] : user.Sex
       // console.log(user_name)
        //console.log(user_age)
       // console.log(user_sex)
        // console.log(userNameRef.current.value, user.FireBaseAuth, userSex['value'], userAge['value']) 
        promisies.push(dispatch(updateUser(user_name, user.FireBaseAuth, user_age, user_sex)))
    }
    // const genreUser = userGenreTypes.map(Genre_Name  => { return {value: Genre_Name.Genre_Name, label:Genre_Name.Genre_Name}})
    if ( userGenre.length > 0){
        const usertypes = userGenre.map( item => { return item.value })
       // console.log(usertypes)
        promisies.push(dispatch(updateUserGenre(usertypes, currentUser.uid)))
      }// genreData.map(Genre_Name  => { return {value: Genre_Name.Genre_Name, label:Genre_Name.Genre_Name}})


    Promise.all(promisies).then(() =>{
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

   <div className='relative w-full h-screen bg-zinc-900/90 '>
        <img src='https://media.istockphoto.com/photos/wooden-brown-books-shelves-with-a-lamp-picture-id1085770318' className="h-full absolute w-full object-cover mix-blend-overlay" />
        <div className='flex items-center justify-center h-auto pt-10 pb-5'>
            {!loading &&
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
                    <input className='rounded-lg border relative  bg-gray-100 p-2' type="text" ref={userNameRef} required  defaultValue={user.Name}/>
                </div>
                <div className='flex flex-col border-none relative pb-2'>
                    <label htmlFor="age">Age</label>
                    <Select key={`stars_${user.Age}`} onChange={handleUserAgeChange} options={ages}  defaultValue={user && ages[returnIndexAge(user.Age)]}/>
                </div>
                <div className='flex flex-col border-none relative pb-2'>
                    <label htmlFor="gender">Sex</label>
                    <Select  key={`stars_${user.Sex}`} onChange={handleUserSexChange} options={sex}  defaultValue={user && sex[returnIndexSex(user.Sex)]} />
                </div>
                <div className='flex flex-col mb-4 border-none relative pb-2'>
                    <label htmlFor="genre">Genre I enjoy reading</label>
                    { !loading_genre && !loading &&
                        <Select  maxMenuHeight={150}   onChange={handleUserGenreChange}  options={genres_short.map(Genre_Name  => { return {value: Genre_Name.Genre_Name, label:Genre_Name.Genre_Name}})} isMulti={true}  defaultValue={user.Usergenre?.map(Genre_Name  => { return  {value: Genre_Name.Genre_Name, label:Genre_Name.Genre_Name}})}/>
                    }
                  
                </div>
                <button disabled={loadingtype}  onClick={handleSubmit} className='w-full my-5 py-2 border relative bg-teal-500 shadow-lg shadow-teal-500/50 hover:shadow-teal-500/40 text-white font-semibold rounded-lg'>Return</button>
                
            </form>}
        </div>
    </div>
  )
}
//defaultInputValue={user.Usergenre.map(Genre_Name  => { return Genre_Name.Genre_Name})} 
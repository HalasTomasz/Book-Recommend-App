import React, {useEffect} from 'react'
import { useAuth } from "../context/AuthContext"
import {useDispatch, useSelector} from 'react-redux'
import {listBookData} from '../actions/bookAction'
import {Link, useParams, useNavigate} from 'react-router-dom'
import ReactStars from "react-rating-stars-component";
import {addToHistory} from '../actions/historyAction'
import {addNewRating} from '../actions/ReviewAction'


export default function BookS(){

    const params = useParams();
    const { currentUser } = useAuth()
    const navigate = useNavigate();
    const dispatch = useDispatch()
    const bookData = useSelector(state => state.bookData)
    const {loading, error, book} = bookData
    console.log(book)
    const ratingChanged = (newRating) => {
      console.log("change")
      dispatch(addNewRating(currentUser.uid,book.Book_ID,newRating))
      };

    function rentBook(){
      try{
        dispatch(addToHistory(currentUser.uid,book.Book_ID))
        navigate('/')
      }catch{
        console.log("ALREADY RENTING THIS BOOK")
      }

    }
    function comeBack(){
      navigate('/')
    }

    useEffect(() => {
        dispatch(listBookData(params.id, currentUser.uid))
      }, [dispatch, currentUser, params.id])

return (
    <div className='w-full min-h-screen bg-gray-500 py-16 px-4'>
      {!loading && 
      <div className='max-w-[1240px] mx-auto grid md:grid-cols-2 gap-x-10'>
        <img className='w-[500px] mx-auto my-4' src={book.ImgSource} alt='/' />
        <div className='flex flex-col justify-center'>
          <p className='font-bold' >{book.Auhtor_Name}</p>
          <h1 className='md:text-4xl sm:text-3xl text-2xl font-bold py-2'>{book.Name}</h1>
          <p>
            {book.Description}
          </p>
          <div className='ml-1 font-bold'>
            Genres:
            <div className='ml-1 underline flex flex-wrap justify-start space-x-2'>
              {book.BookGenre?.map((item, id) => {
                  return (
                  <p key={id}> {item.Genre_Name} </p>
                  );
              })}
            </div>
          </div>
          <div className='flex flex-row py-3 max-sm:space-x-2 space-x-4  text-base'>
            <div className='font-bold max-lg:text-sm max-sm:text-xs '> Book is {book.Availability > 0 ? 'Available' : 'Unavailable'}</div> 
            <div className='flex flex-row'>
              <p className='grow-1 font-bold max-lg:text-sm max-sm:text-xs '> {book.Rating} of 5</p> 
              <svg aria-hidden="true" className="w-5 h-5 text-yellow-400 justify-center" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><title>First star</title><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
            </div>
            <a className="max-lg:text-sm max-sm:text-xs text-gray-900 underline hover:no-underline dark:text-white">{book.NumberReviews} reviews</a>
            </div>
        <div className='flex items-center lg:mr-4 px-2'> 
            <p className='mr-5 font-bold'> Your rating:</p>
            <div className='md:w-auto'>
            <ReactStars
                key={`stars_${book.Review}`}
                count={5}
                onChange={ratingChanged}
                size={24}
                isHalf={true}
                value={book.Review} // COŚ SIEZ JEBAŁO TUTAJ
                emptyIcon={<i className="far fa-star"></i>}
                halfIcon={<i className="fa fa-star-half-alt"></i>}
                fullIcon={<i className="fa fa-star"></i>}
                activeColor="#ffd700"
            /> 
            </div>
          </div>
          <div className='grid grid-cols-2'>
            { book.Availability ?
              <button onClick={rentBook} disabled={book.Availability === 0}  className='bg-black text-[#00df9a] w-auto inline-block rounded-md font-medium my-6 py-3'>Wypożycz</button> :
              <button onClick={rentBook} disabled={book.Availability === 0}  className='bg-gray-400 text-[#00df9a] w-auto inline-block rounded-md font-medium my-6 py-3 '>Wypożycz</button> }
              

            <button onClick={comeBack}  className='bg-black text-[#00df9a] w-auto inline-block rounded-md font-medium my-6 ml-5 py-3'>Powrót</button>
          </div>
        </div>
      </div>
      }
    </div>
  );
};
 

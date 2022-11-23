import React, {useEffect} from 'react'
import {Link, useParams,useLocation, isRouteErrorResponse} from 'react-router-dom'
import {useDispatch, useSelector} from 'react-redux'
import { useAuth } from "../context/AuthContext"
import {getListHistory} from '../actions/historyAction'
import HistoryRow from '../components/HistoryRow'

export default function HistoryS() {
    const params = useParams()
    const book_id = params.id
    const { currentUser } = useAuth()
    const location = useLocation()
    const user_id = location.state ? Number(location.state) : 1
    const dispatch = useDispatch()
    const user_history = useSelector(state => state.getUserHistory.user_history)
    //const {error,loading, user_history} = history

    useEffect(()=> {
       dispatch(getListHistory(currentUser.uid))
    },[dispatch])

  return (
      <div className='bg-gray-500 h-screen'>
            <h1 className='flex justify-center text-4xl font-bold pb-6 pt-3'>Book Rental History</h1>
            {user_history.length === 0 ?(
                <div className='flex justify-center space-x-2 items-center'>
                    <h2 className='text-2xl'> You dont have any books take</h2>
                    <Link className='text-base underline' to='/'> Go Back</Link> 
                </div>
                ) :
                ( 
                <div className=''>
                    <HistoryRow list = {user_history} />
                </div>
            )}
    </div>
  );
};
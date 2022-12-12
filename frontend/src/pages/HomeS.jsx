import React from 'react'
import Row from '../components/Row.jsx'
import {useState, useEffect} from 'react'
import { useAuth } from '../context/AuthContext.js'
import {useDispatch, useSelector} from 'react-redux'
import {getUserRecomendation} from '../actions/userAction'

function HomeS() {

  const dispatch = useDispatch()
  const { currentUser } = useAuth()
  const alg_data =  useSelector(state => state.getUserDataAlgo)
  const {loading, error, recomendation} = alg_data
  console.log(loading)
   // const {loading, error, recomendation} = useSelector(state => state.getUserDataAlgo)
  useEffect(() => {
      dispatch(getUserRecomendation(currentUser.uid))
  }, [currentUser, dispatch])

  return (
  <div className='bg-gray-500'>
       {!loading && <Row  rowID='1' title='First Algorithm OR MIX '  list = {recomendation}/> }
       {!loading && <Row  rowID='2' title='Second Algorithm OR MIX ' list = {recomendation}/> }
       {/* !loading && <Row  rowID='3' title='Third  Algorithm OR MIX ' list = {recomendation}/>  */}
       {/*!loading && <Row  rowID='4' title='STH Algorithm OR MIX ' list = {recomendation} /> */ }
    </div>
  )
}

export default HomeS
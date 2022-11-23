import React from 'react'
import Row from '../components/Row.jsx'
import {useState, useEffect} from 'react'

import {useDispatch, useSelector} from 'react-redux'
import {listBooks} from '../actions/bookAction'

function HomeS() {
  const dispatch = useDispatch()
  const bookList = useSelector(state => state.bookList)
  const {error, loading, books} = bookList

  useEffect(() => {
    dispatch(listBooks())
  },[])

  return (
    <div className='bg-gray-500'>
        <Row  rowID='1' title='First Algorithm OR MIX '  list = {books}/>
        <Row  rowID='2' title='Second Algorithm OR MIX ' list = {books}/>
        <Row  rowID='3' title='Third  Algorithm OR MIX ' list = {books}/>
        <Row  rowID='4' title='STH Algorithm OR MIX ' list = {books} />
      </div>
  )
}

export default HomeS
import React from 'react'
import Row from '../components/Row.jsx'
import BookCard from '../components/BookCard.jsx'
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
    <div>
        <Row title='First Algorithm OR MIX '  list = {bookList}/>
        <Row title='Second Algorithm OR MIX ' list = {bookList}/>
        <Row title='Third  Algorithm OR MIX ' list = {bookList}/>
        <Row title='STH Algorithm OR MIX ' list = {bookList} />
      </div>
  )
}

export default HomeS
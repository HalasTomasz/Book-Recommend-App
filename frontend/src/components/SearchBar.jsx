import React, { useState, useEffect} from "react";
import {BiSearch} from 'react-icons/bi'
import {useDispatch, useSelector} from 'react-redux'
import {listBooks} from '../actions/bookAction'

export default function SearchBar() {

    const [filterOnData, setFilterOnData] = useState([]);
    const [words, setWords] = useState("");
    const dispatch = useDispatch()
    const bookList = useSelector(state => state.bookList)
    const {error, loading, books} = bookList
  
    useEffect(() => {
      dispatch(listBooks())
    },[dispatch])

    const handleFilter = (event) => {
        const wordWeLookFor = event.target.value;
        setWords(wordWeLookFor); 
        const newFilter = books.filter((value) => {
          return value.Name.toLowerCase().includes(words.toLowerCase());
        })
        console.log(newFilter)
        if (wordWeLookFor === "") {
            setFilterOnData([]);
        } else {
            setFilterOnData(newFilter);
        }};
      
        const clearInput = () => {
            setFilterOnData([]);
            setWords("");
        };
      
        return (
          <div className="grid h-screen justify-center items-center bg-gray-500">
            <div className="w-full flex justify-between items-center border-b-2 border-gray-200 py-1 px-4">
              <div className="relative hidden md:block">
                  <form className='absolute md:static top-10 -left-20 bg-white'>
                      <input
                          value={words}
                          onChange={handleFilter}
                          className='bg-primary p-3 md:text-md font-medium border-2 border-gray-100 focus:outline-none focus:border-2 focus:border-gray-300 w-[300px] md:w-[350px] rounded-full  md:top-0'
                          placeholder='Szukaj ogloszen'
                      />
                      <button
                          //onClick={handleSearch}
                          className='absolute md:right-5 right-6 top-4 border-l-2 border-gray-300 pl-4 text-2xl text-gray-400'
                      >
                          <BiSearch />
                      </button>
                  </form>
              </div>
            </div>
            {filterOnData.length != 0 && (
              <div className="bg-white  overflow-hidden">
                {filterOnData.slice(0, 6).map((value, key) => {
                  return (
                    <a className="" href={`/books/${value.Book_ID}`} target="_blank">
                      <p>{value.Name} </p>
                    </a>
                  );
                })} 
              </div>)}
            </div>
        );
      }
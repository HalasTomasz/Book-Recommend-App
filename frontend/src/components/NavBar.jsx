import React, {useState, useContext} from 'react'
import { AiOutlineMenuUnfold,AiOutlineClose } from 'react-icons/ai';
import {Link, useNavigate} from 'react-router-dom';
import { useAuth } from "../context/AuthContext"

function Navbar(){
  
  const [nav,setNav] = useState(false)
  const { currentUser, logout } = useAuth()
  const navigate = useNavigate();
  const [error, setError] = useState("")

  function changeNav() {
    setNav(prevState => !prevState)
  }

  async function logUserOut(e) {
    e.preventDefault()
    setError("")
    try {
     
      await logout()
      navigate('/');
    } catch {
 
    }
  }

  return (
    <header className=' w-full bg-gray-700'>
      <div className='justify-between mx-auto items-center h-24 flex max-w-screen-lg px-4 bg-gray-700'>
        <h1 className='text-[#00df6e] font-bold text-2xl md:text-xl lg:text-2xl p-2'>Bibliophile's Tool</h1>
        <ul className='hidden md:flex'>
          <li className='p-3'>
            <Link to={"/"} className='text-[#00df6e] text-base'>Home</Link>
          </li>
          <li className='p-3'>
            <Link to={"/search"} className='text-[#00df6e]  text-base'>Search Browser</Link>
          </li>
          <li className='p-3'>
            <Link to={"/user"} className='text-[#00df6e]  text-base'>User Profile</Link>
          </li>
          <li className='p-3'>
            <Link to={"/history"} className='text-[#00df6e]  text-base'>History</Link>
          </li>
          <li className='p-3'>
            <Link to={"/about"} className='text-[#00df6e]  text-base'>About</Link>
          </li>
          <li className='p-3 text-[#00df6e]  text-base' >
            <Link to={"/"} onClick={logUserOut}>Logout</Link>
          </li>
        </ul>
        <div onClick={changeNav} className='md:hidden flex right-0 '>
          {!nav ? <AiOutlineMenuUnfold size={28} /> : <AiOutlineClose size={28}/>}
         </div>
         <ul className={nav ? 'md:hidden top-0 left-0 absolute z-10 w-[60%] h-max border-r border-r-gray-900  bg-gray-700 ease-in-out duration-100 ':' ease-in-out duration-500 fixed left-[-100%]'}>
            <h1 className='text-[#00df6e] p-3 mt-6 ml-2 text-2xl font-bold'>Bibliophile's Tool</h1>
            <li className='p-4 border-b ml-4 hover:bg-slate-100 border-t-4 border-grey-900'  > <Link to={"/"} className='text-[#00df6e]  text-base'>Home</Link></li>
            <li className='p-4 border-b ml-4  hover:bg-slate-100' ><Link to={"/search"} className='text-[#00df6e]  text-base'>Search Browser</Link></li>
            <li className='p-4 border-b ml-4  hover:bg-slate-100'><Link to={"/user"} className='text-[#00df6e]  text-base'>User Profile</Link></li>
            <li className='p-4 border-b ml-4  hover:bg-slate-100'><Link to={"/history"} className='text-[#00df6e]  text-base'>History</Link></li>
            <li className='p-4 border-b ml-4 hover:bg-slate-100'><Link to={"/about"} className='text-[#00df6e]  text-base'>About</Link></li>
            <li className='p-4 border-b ml-4  hover:bg-slate-100 text-[#00df6e]' >
            <Link to={"/"} onClick={logUserOut}>Logout</Link>
          </li>
         </ul>
      </div>
      
    </header>
  )
}

export default Navbar

import React, {useState} from 'react'
import { Link } from 'react-router-dom';
import { NavbarData } from './NavbarData';
import './Navbar.css';
import { IconContext } from 'react-icons';
import { Container, Row, Col } from "shards-react";

import {withRouter} from 'react-router-dom';

function Navbar(props) {
    

    return (
    <div className="nav-menu">
        
        <ul className='nav-menu-items'>
            {NavbarData.map((item, index) => {
            const pathname = window.location.pathname;
            console.log(pathname);
            if(pathname == item.path)
                return(
                    <IconContext.Provider value={{ color: item.selectColor }}>
                        <li key={index} className={item.cName}>
                            <Link to={item.path}>
                                {item.icon}
                                <span style={{color: item.selectColor}}>{item.title}</span>
                            </Link>
                        </li>
                    </IconContext.Provider>
                    )
                
            return (
                <IconContext.Provider value={{ color: '#8c8c8c' }}>
                    <li key={index} className={item.cName}>
                        <Link to={item.path}>
                            {item.icon}
                            <span>{item.title}</span>
                        </Link>
                    </li>
                </IconContext.Provider>
            );
            })}
        </ul>
        
    </div>
    );
  }

export default Navbar

//import useState hook to update selected menu item
import React, { useState } from "react";
import ProfileCard from './ProfileCard';
import { Link } from 'react-router-dom';

//import react pro sidebar components
import {ProSidebar, Menu, MenuItem, SidebarHeader, SidebarFooter, SidebarContent} from "react-pro-sidebar";

//import icons from react icons
import { RiSwordLine } from "react-icons/ri";
import { FiHome, FiCamera, FiLogOut} from "react-icons/fi";


import "react-pro-sidebar/dist/css/styles.css";
import "./Navbar.css";
import prof_photo from "../images/prof.jpg";



const Navbar = () => {
  
    // Function gets called when logout is clicked
    const logoutClicked = () => {
        alert("\n You think you can leave... how cute"); 
    }

    // Create hook to update when new selection is made
    const [itemSelected, setItemSelected] = useState(false)

    // A simple state that changes on click to force a render of componenet
    const menuItemSelect = () => {
        itemSelected ? setItemSelected(false) : setItemSelected(true);
    };


    return (
        <>
            <div id="navbar">
                <ProSidebar collapsed={false}>
                <SidebarHeader>
                   <ProfileCard image={prof_photo} username="Ben_Johnson" level="12"/>
                </SidebarHeader>
                <SidebarContent>
                    <Menu iconShape="square">
                        <div className="home-menuItem">
                        <MenuItem className="home-menuItem" active={window.location.pathname == "/"} onClick={menuItemSelect} icon={<FiHome className="home-menuText"/>}>
                            <div className="menu-text">Home</div>
                            <Link to="/" />
                        </MenuItem>
                        </div>
                        <div className="observation-menuItem">
                        <MenuItem className="observation-menuItem" active={window.location.pathname == "/observations"} onClick={menuItemSelect} icon={<FiCamera className="observation-menuText"/>}>
                            <div className="menu-text">Observations</div>
                            <Link to="/observations" />
                        </MenuItem>
                        </div>
                        <div className="battle-menuItem">
                        <MenuItem className="battle-menuItem" active={window.location.pathname == "/battle"} onClick={menuItemSelect} icon={<RiSwordLine className="battle-menuText"/>}>
                            <div className="menu-text">Battle</div>
                            <Link to="/battle" />
                        </MenuItem>
                        </div>
                    </Menu>
                </SidebarContent>
                <SidebarFooter>
                    <Menu iconShape="square">
                    <MenuItem onClick={logoutClicked} icon={<FiLogOut />}> <div className="logout-text">Logout</div></MenuItem>
                    </Menu>
                </SidebarFooter>
                </ProSidebar>
            </div>
        </>
    );
};

export default Navbar;
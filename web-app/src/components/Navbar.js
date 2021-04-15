//import useState hook to create menu collapse state
import React, { useState } from "react";

//import react pro sidebar components
import {
  ProSidebar,
  Menu,
  MenuItem,
  SidebarHeader,
  SidebarFooter,
  SidebarContent,
} from "react-pro-sidebar";

import { Link } from 'react-router-dom';

//import icons from react icons
import { RiSwordLine } from "react-icons/ri";
import {FaRegHeart } from "react-icons/fa";
import { FiHome, FiCamera, FiLogOut} from "react-icons/fi";
import { RiPencilLine } from "react-icons/ri";
import { BiCog } from "react-icons/bi";


//import sidebar css from react-pro-sidebar module and our custom css 
import "react-pro-sidebar/dist/css/styles.css";

import "./Navbar.css";


const Navbar = (props) => {
  
    /*
    //create initial menuCollapse state using useState hook
    const [menuCollapse, setMenuCollapse] = useState(false)
    
    //create a custom function that will change menucollapse state from false to true and true to false
    const menuIconClick = () => {
    //condition checking to change state from true to false and vice versa
        menuCollapse ? setMenuCollapse(false) : setMenuCollapse(true);
    }; 

    setMenuCollapse(false);
    */

    //create initial menuCollapse state using useState hook
    const [itemSelected, setItemSelected] = useState(false)

    //create a custom function that will change menucollapse state from false to true and true to false
    const menuItemSelect = () => {
    //condition checking to change state from true to false and vice versa
        itemSelected ? setItemSelected(false) : setItemSelected(true);
    };


    return (
        <>
            <div id="navbar">
                {/* collapsed props to change menu size using menucollapse state */}
                <ProSidebar collapsed={false}>
                <SidebarHeader>
                <div className="logotext">
                    {/* small and big change using menucollapse state */}
                    <p> Big Logo </p>
                </div>
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
                    <MenuItem icon={<FiLogOut />}> <div className="logout-text">Logout</div></MenuItem>
                    </Menu>
                </SidebarFooter>
                </ProSidebar>
            </div>
        </>
    );
};

export default Navbar;
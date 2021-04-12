import React from 'react';
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import * as IoIcons from 'react-icons/io';
import * as RiIcons from 'react-icons/ri';

export const NavbarData = [
  {
    title: 'Dashboard',
    path: '/',
    icon: <AiIcons.AiFillHome />,
    selectColor: '#ff0000',
    cName: 'nav-text'
  },
  {
    title: 'Observations',
    path: '/observations',
    icon: <FaIcons.FaPaw />,
    selectColor: '#0000ff',
    cName: 'nav-text'
  },
  {
    title: 'Battle',
    path: '/battle',
    icon: <RiIcons.RiSwordFill />,
    selectColor: '#ffff00',
    cName: 'nav-text'
  },
  {
    title: 'Settings',
    path: '/settings',
    icon: <IoIcons.IoMdSettings />,
    selectColor: '#00ffff',
    cName: 'nav-text'
  }
];
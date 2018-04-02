// menu.js

var closing;

// Menu Positioning
rootStyleDisplay = "block";
rootStylePosition = "absolute";
rootStyleLeft = "0px";
rootStyleTop = "100px";

// Relative position of menuitem
styleLeft = "125px";
styleTop = "-1px";

menuitemIsOpen = false;

function switchMenu(aObj,show)
{
  var menuItem = aObj;
  if(show)
  {
    // Hilight on
    menuItem.className = "menuItemHi";
    // Stop closing
    window.clearTimeout(closing);
  }
  else
  {
    // Hilight off
    menuItem.className = "menuItem";
    // Start closing    
    closing = window.setTimeout("closeMenu('root')",1500);
  }
  // Close other open menus on the same level
  closeOtherMenus(menuItem);
  // Check for submenu
  if(getSubMenu(menuItem,false))
  {
    // Get parent menuContainer
    parentMenuCon = menuItem.parentNode;
    subMenuCon = getSubMenu(menuItem,true); 
    // Show submenu
    if(show)
    {
      subMenuCon.style.display = "block";
      subMenuCon.style.position = "absolute";
      subMenuCon.style.left = styleLeft;
      subMenuCon.style.top = styleTop;
    }
  }
}

function closeMenu(menu)
{
  // Get root element
  if(menu=="root")
  {
    menu = document.getElementById("rdmenu");
  }
  if (menu)
  {
    var menuItems = menu.childNodes;
    // Go into every child node
    for(var i=0;i<menuItems.length;i++)
    {
      if(getSubMenu(menuItems[i],false))
      {
        var subMenu = getSubMenu(menuItems[i],true); 
        // Hide subMenu 
        //alert(subMenu)
        subMenu.style.display = "none";
        // Start recursion for submenu
        closeMenu(subMenu);
      }
    }
  }
}

function getSubMenu(menuItem,returnObject)
{
  //Returns the submenu object of a menuItem
  for(i=0;i<menuItem.childNodes.length;i++)
  {
    if(menuItem.childNodes[i].className == "menuContainer")
    {
      if (returnObject)
      {
        return menuItem.childNodes[i];
      }
      else
      {
        return true;
        break;
      }
    }
  }
  return false;
}

function closeOtherMenus(menuItem)
{
  // Get menu element
  var menu = menuItem.parentNode;
  var parentMenuItems = menu.childNodes;
  // Go into every child node
  for(var i=0;i<parentMenuItems.length;i++)
  {
    if(getSubMenu(parentMenuItems[i],false) && parentMenuItems[i]!=menuItem)
    {
      var subMenu = getSubMenu(parentMenuItems[i],true);
      // Hide subMenu 
      subMenu.style.display = "none";
      // Start recursion for submenu
      closeMenu(subMenu);
    }
  }
}

function rdInitMenu()
{
  rootObj = document.getElementById("rootMenuContainer");
  rootObj.style.display = rootStyleDisplay;
  rootObj.style.position = rootStylePosition;
  rootObj.style.left = rootStyleLeft;
  rootObj.style.top = rootStyleTop;
}

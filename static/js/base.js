// Foreign Key ADD popup function
function showAddPopup(triggeringLink, title = "Add Form", h = 500, w = 800) {
    var name = triggeringLink.id.replace(/^add_/, '');
    console.log("in add form")
    url = triggeringLink.href;

    var width = window.innerWidth ? window.innerWidth : document.documentElement.clientWidth ? document.documentElement.clientWidth : screen.width;
    var height = window.innerHeight ? window.innerHeight : document.documentElement.clientHeight ? document.documentElement.clientHeight : screen.height;
    var left = ((width / 2) - (w / 2));
    var top = ((height / 2) - (h / 2));
    var newWindow = window.open(url, title, 'scrollbars=yes, width=' + w + ', height=' + h + ', top=' + top + ', left=' + left);
    if (window.focus) {
        newWindow.focus();
    }
    return false;
}
// Foreign Key CLOSE popup function
function closeAddPopup(win, newID, newRepr, id) {
    $(id).val(newRepr)
    win.close();
}
const onGetTitleMessagueFromCategory = category=>{
    const titles = {
        'success':'bien echo',
        'warning':'Atencion',
        'info':'Atencion',
        'error':'Oops....!'
    }
    return titles[category]
}
function onGetShowMessage(categoria, message){
    Swal.fire({
        icon: categoria,
        title: onGetTitleMessagueFromCategory(categoria),
        text: message
    })
}
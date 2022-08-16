function deleteMsg(msg)
{
	var ans = window.confirm(msg);
	if(!ans)
	{
	  event.preventDefault();
	}
}
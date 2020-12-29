let funzr =document.addEventListener('click',
  function ()
  {
  let id=document.querySelectorAll("#id");
  let test=event.target
  eve(test.value)
  document.querySelector('#show').innerHTML=' ';
  });
   
  function eve(id)
  {
    let div=document.querySelector('#show');
  fetch(`/${id}/reports`,
  {
    method:"GET"
  })
  .then(response=>response.json())
  .then(response=>{
    response.forEach(element => {
      let p=document.createElement('p');
      p.append(element);
      div.appendChild(p)
    });
  })

  }
var dataList = document.getElementById('data-list')
var showAllBtn = document.getElementById('show-all-btn')
      
    showAllBtn.addEventListener('click', function () {
        if (dataList.style.display === 'none') {
          dataList.style.display = 'block'
        } else {
          dataList.style.display = 'none'
        }
    })
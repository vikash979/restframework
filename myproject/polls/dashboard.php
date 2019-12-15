<!DOCTYPE html>

  <body class="app sidebar-mini rtl">
    <!-- Navbar-->

    <!-- Sidebar menu-->
  <link href="<?php echo base_url();?>admin/docs/css/bootstrap.min.css" rel="stylesheet" />
    <main class="app-content">
      <div class="app-title">
        <div>
          <h1><i class="fa fa-edit"></i> School Atttendence</h1>

        </div>
        <ul class="app-breadcrumb breadcrumb">
          <li class="breadcrumb-item"><i class="fa fa-home fa-lg"></i></li>
          <li class="breadcrumb-item">School</li>
          <li class="breadcrumb-item"><a href="#">School Atttendence</a></li>
        </ul>
      </div>
      <div class="row">

        <div class="col-md-12">

          <div class="tile">

            <div class="tile-body">
              <div class="col-md-6" >
                <div class="form-group">
                  <div class="col-md-2">
                 <label>Class</label>
               </div>
               <div class="col-md-10">
                 <select name="std_religion" id="std_religion" class="form-control" onchange="showsec(this.id,this.value);"  />
                 <option value="">--Select Class--</option>
                 <?php
                  foreach ($clas as $cln)
                  {
                  ?>

                 <option value="<?php echo $cln['class_name'];?>"><?php echo $cln['class_name'];?></option>
                 <?php
               }
                  ?>
               </select>
<input type="hidden" id="clanme" value="">
                </div>
              </div>
              </div>
              <div class="col-md-6" style="display:" id="std_section" >
                <div class="form-group">
                  <div class="col-md-2">
                 <label>Section</label>
               </div>
               <div class="col-md-10">
                 <select name="std_sec" id="std_sec" class="form-control" onchange="showtabl(this.value,'clanme')" />

                 <option value="">--Select Section--</option>
                 <?php
                  foreach ($sec as $scr)
                  {
                  ?>
                 <option value="<?php echo $scr['sec_name'];?>"><?php echo $scr['sec_name'];?></option>
                 <?php
               }
                ?>


               </select>
                 <span id="error_rel" class="text-danger"></span>
                </div>
              </div>
              </div>


            </div>
            <div class="tile-footer">
              <div class="row">
                <div class="col-md-12" id="stdac" style="display:none">
                         <div class="tile">
                           <div class="tile-body">
                             <table class="table table-hover table-bordered" id="sampleTable" >
                               <thead>
                                 <tr>
                                   <th>Name</th>
                                   <th>Position</th>
                                   <th>Office</th>
                                   <th>Age</th>
                                   <th>Start date</th>
                                   <th>Salary</th>
                                 </tr>
                               </thead>
                               <tbody >

                               </tbody>
                             </table>

                           </div>
                         </div>
                       </div>
              </div>
            </div>
          </div>
        </div>
        <div class="clearix"></div>

      </div>
    </main>
    <script>
function showsec(id,val)
{
  var std_section=document.getElementById("std_section")
  if(val!='')
  {

  std_section.style.display='block';
  $('#clanme').val(val)
}
else {
  std_section.style.display='none';
}
}
function showtabl(val,idd)
{
var ids=document.getElementById(idd).value
var stdac=document.getElementById("stdac");
stdac.style.display='block';

$.ajax({

url:  "<?php echo base_url("index.php/Students/stulist");?>",
type : "POST",

data : {"clas" : ids, "sect" : val},
success: function(msg){
//  window.location.href = "http://localhost/CodeIgniters/index.php/Students/stulistt";

//alert("Updated SuccessFully")
$("#stdac").html(msg);
$('#cless').val(ids)
$('#seess').val(val)
}
});
}
    </script>
    <!-- Essential javascripts for application to work-->

  </body>
</html>

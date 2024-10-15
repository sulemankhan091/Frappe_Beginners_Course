// Copyright (c) 2024, Muhammad Suleman and contributors
// For license information, please see license.txt

frappe.ui.form.on("Clientside Scripting", {
	// refresh(frm) {
      // frappe.msgprint("Hello Dcode Website")
      // frappe.throw("This is error message")
    // }

      
    validate:function(frm){
      // frm.set_value('fullname',frm.doc.firstname+" "+ frm.doc.middlename+" "+frm.doc.lastname)


      // let row = frm.add_child('family_member',{
      //   name1:"Ali",
      //   age:12,
      //   relation:'son',
      // })

      

      
    },
    // after_save:function(frm){
    //   frappe.msgprint(__(`The Fullname is '{0}'`),[
    //     frm.set_value('fullname',frm.doc.firstname+" "+ frm.doc.middlename+" "+frm.doc.lastname)
    //   ])
    // },
    // refresh:function(frm){
      // frm.set_intro('Now you can save this document');

      // if(frm.is_new()){
      // frm.set_intro('Now you can create new client side scripting ');
      // }
    // }


    // Some events

    
    
});
  
// Child table scripting
  frappe.ui.form.on('Family Members',{

    // name1:function(frm){
    //   frappe.msgprint("Hello Dcode from  child doctype name1 Event")
    // }
  })

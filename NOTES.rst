Assumptions:

* Fields will only be fertilized once. This is true for the sample events, but likely wouldn't be in practice. 
* I'm not actually deleting users on user:delete because I want to maintain the record of which users performed certain actions such as planting or fertilizing. Instead I set a deleted attribute and don't allow them to be used for subsequent actions.
* I am however deleting fields on field:delete. The assumption is you don't care about a field anymore after deleting it.

Places to improve:

* Input validation. At this point I'm mostly assuming the events are valid, but in a production system there would be much more validating and matching tests.
* Authentication. In a real system we'd need to authenticate users and verify that they had permissions to modify a field.

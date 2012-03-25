PLIP Implementation
===================

Create a buildout configuration file for your plip in the 'plips' folder.
Give it a descriptive name, starting with the plip number;
'plip-1234-widget-frobbing.cfg' for example. This file will define the
branches/trunks you're working with in your PLIP. It should look something
like this:

In file plips/plip-1234-widget-frobbing.cfg...::

 [buildout]
 extends = plipbase.cfg
 auto-checkout +=
  plone.somepackage
  plone.app.someotherpackage

 [sources]
  plone.somepackage = git git://github.com/plone/plone.somepackage.git branch=plip-1234-widget-frobbing
  plone.app.someotherpackage = git git://github.com/plone/plone.app.somepackage.git branch=plip-1234-widget-frobbing

 [instance]
 eggs +=
    plone.somepackage
    plone.app.someotherpackage
 zcml +=
    plone.somepackage
    plone.app.someotherpackage

Use the same naming convention when branching existing packages, and you
should always be branching packages when working on PLIPs.


What is a PLIP? 
A PLIP is a PLone Improvement Proposal. It is a change to a Plone package that would affect everyone. PLIPs go through a different process than bug fixes because of their broad reaching effect. The Plone 4.x Framework Team reviews all PLIPs to be sure that it’s in the best interest of the broader community to be implemented and that it is of high quality.
Is it a PLIP or a bugfix?
In general, anything that changes the API of Plone in the backend or UI on the front end should be filed as a PLIP. When in doubt, submit it as a PLIP. The framework team is eager to reduce it’s own workload and will re-classify it for you.
Who can submit PLIPs?
Anyone who has signed a Plone core contributor agreement can work on a PLIP. Don’t let the wording freak you out: signing the agreement is easy and you will get access almost immediately.
You do not have to be the most amazing coder in the entire world to submit a PLIP. The Framework Team is happy to help you at any point in the process. Submitting a PLIP can be a great learning process and we encourage people of all backgrounds to submit.  When the PLIP is accepted, a Framework Team member will “champion” your PLIP and be dedicated to seeing it completed.
PLIPs are not just for code monkeys. If you have ideas on new interactions or UI your ideas are more than welcome. We will even help you pair up with implementors if needed.
What is a PLIP champion?
When you submit your PLIP and it is approved, 1 Framework Team member who is especially excited about seeing the PLIP completed will be assigned to your PLIP as a champion. They are there to push you through completion as well as answer any questions and provide guidance. 
Keep in mind that champions are in passive mode by default. If you need help or guidance, please reach out to them as soon as possible to activate help mode. 
I’m still nervous. Can I get involved other ways at first?
If you want to feel the process and how it works, help us review PLIPs as the implementations finish up. Simply ask on  of the Framework Team members what PLIPs are available for review or check the status of PLIPs at XXX:Link. Make sure to let us know you intend to review the PLIP by joining the Framework Team mailing list (XXX:link) and sending a quick email.
Then, follow the simple instructions for reviewing a PLIP (XXX:link). Thank you in advance!
When can I submit a PLIP?
Today, tomorrow, any time! After the PLIP is accepted, the Framework Team will try to judge complexity and time to completion and assign it to a milestone. You can begin working immediately, and we encourage submitting fast and furious.
When is the PLIP due?
Summary: As soon as you get it done.
&tldr; Technically, we want to see it completed for the release to which it’s assigned. We know that things get busy and new problems make PLIPs more complicated and we will push it to the next release. 
In general, we don’t want to track a PLIP for more than a year. If your PLIP is accepted and we haven’t seen activity in over a year, we will probably ask you to restart the whole process.
You don’t like my PLIP :( What now?
Just because a PLIP isn’t accepted in core doesn’t mean it’s a bad idea. It is often the case that there are competing implementations and we want to see it vetted as an add on before “blessing” a preferred implementation. 

PLIP Process Overview
Submit a PLIP
PLIP is Approved
Setup PLIP branch and implement PLIP

Submit PLIP for review
Framework Team reviews plip and give feedback
Address concerns in feedback and resubmit. This may go back and forth a few times.
PLIP is approved and merged. The PLIP may be rejected and closed, but this is very rare for those who stick though the process.

How to Submit a PLIP
Whether you want to update the default theme or rip out a piece of architecture, everyone should go through the following process. If you need help at any point in this process, please contact a member of the framework team personally or ask for help on the FWT mailing list XXX: link here.
First and foremost, solicit feedback on your idea on the plone-developers mailing list. In this vetting process, you want to make sure that the change won’t adversely affect other people on accident. Others may be able to point out risks or even offer up better or existing solutions. 
When you are happy with the feedback, submit a PLIP. XXX: Link here. Please use the template provided (XXX: put the template here? Can we just have a custom ticket type?). Please note a few things. It is very rare that the “Risks” section will be empty or none. If you find this is the case and your PLIP is anything more than trivial, maybe some more vetting should be done. 
The seconder field is REQUIRED. We will send the PLIP back to you if it is not filled in. Currently, this is just someone else who thinks your PLIP is a good idea, a +1. In the near future, we will start asking that the seconder is either a coding partner, or someone who is willing and able to finish the PLIP should something happen to the implementor.

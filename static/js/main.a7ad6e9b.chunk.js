(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{176:function(e,t,n){e.exports=n(369)},181:function(e,t,n){},369:function(e,t,n){"use strict";n.r(t);var a=n(1),s=n.n(a),i=n(7),o=n.n(i),l=(n(181),n(174)),r=n(21),c=n(22),h=n(25),u=n(23),d=n(16),g=n(24),p=(n(55),n(374)),L=n(380),m=n(381),C=n(40),y=n(373),S=n(377),D=p.a.Title,f=function(e){function t(e){var n;return Object(r.a)(this,t),(n=Object(h.a)(this,Object(u.a)(t).call(this,e))).onChange=n.onChange.bind(Object(d.a)(n)),n}return Object(g.a)(t,e),Object(c.a)(t,[{key:"onChange",value:function(e){this.props.jumpTo(e)}},{key:"render",value:function(){var e=this;return s.a.createElement(L.a,{style:{overflow:"hidden",whiteSpace:"nowrap"}},s.a.createElement(m.a,{span:10},s.a.createElement(D,null,"TOMASULO\u7b97\u6cd5\u6a21\u62df\u5668(\u5468\u671f",this.props.currentCycle,"/",this.props.allCycle,")")),s.a.createElement(m.a,{span:4},"\u8bbe\u7f6e",s.a.createElement(y.a,{checkedChildren:"\u5f00",unCheckedChildren:"\u5173",defaultChecked:!1,onChange:function(){return e.props.changeSettings()}}),"\u53d1\u5c04\u8868",s.a.createElement(y.a,{checkedChildren:"\u5f00",unCheckedChildren:"\u5173",defaultChecked:!0,onChange:function(){return e.props.changeIssueTable()}})),s.a.createElement(m.a,{span:7},s.a.createElement(C.a,{onClick:function(){return e.props.handleBefore()}},"\u540e\u9000"),s.a.createElement(C.a,{onClick:function(){return e.props.handleNext()},style:{marginLeft:"30px"}},"\u524d\u8fdb"),s.a.createElement(S.a,{min:1,max:this.props.allCycle,defaultValue:this.props.currentCycle,style:{marginLeft:"50px"},onChange:this.onChange}),s.a.createElement(C.a,{onClick:function(){return e.props.handleJump()},style:{marginLeft:"30px"}},"\u8df3\u8f6c")),s.a.createElement(m.a,{span:3,style:{paddingRight:"0px"}},s.a.createElement(C.a,{onClick:this.props.onClick,type:"primary"},"\u4f20\u5165NEL\u7a0b\u5e8f"),s.a.createElement(C.a,{onClick:this.props.onClickTest,style:{marginLeft:"5px"}},"\u6d4b\u8bd5\u8fde\u63a5")))}}]),t}(a.Component),A=n(45),U=n.n(A),k=function(e){function t(){return Object(r.a)(this,t),Object(h.a)(this,Object(u.a)(t).apply(this,arguments))}return Object(g.a)(t,e),Object(c.a)(t,[{key:"render",value:function(){return s.a.createElement("div",null,s.a.createElement(U.a,{dataSource:this.props.dataSource,columns:this.props.columns,bordered:!0,pagination:!1}))}}]),t}(a.Component),b=function(e){function t(){return Object(r.a)(this,t),Object(h.a)(this,Object(u.a)(t).apply(this,arguments))}return Object(g.a)(t,e),Object(c.a)(t,[{key:"render",value:function(){return s.a.createElement("div",null,s.a.createElement(U.a,{dataSource:this.props.dataSource,columns:this.props.columns,bordered:!0,pagination:!1,scroll:{x:1300}}))}}]),t}(a.Component),v=function(e){function t(){return Object(r.a)(this,t),Object(h.a)(this,Object(u.a)(t).apply(this,arguments))}return Object(g.a)(t,e),Object(c.a)(t,[{key:"render",value:function(){return s.a.createElement("div",null,s.a.createElement(U.a,{dataSource:this.props.dataSource,columns:this.props.columns,bordered:!0,pagination:!1}))}}]),t}(a.Component),R=function(e){function t(e){var n;return Object(r.a)(this,t),(n=Object(h.a)(this,Object(u.a)(t).call(this,e))).state={dataSource:[{key:"1",name:"\u80e1\u5f66\u658c",age:32,address:"\u897f\u6e56\u533a\u6e56\u5e95\u516c\u56ed1\u53f7"},{key:"2",name:"\u80e1\u5f66\u7956",age:42,address:"\u897f\u6e56\u533a\u6e56\u5e95\u516c\u56ed1\u53f7"}],columns:[{title:"\u4fdd\u7559\u7ad9",dataIndex:"name",key:"name"},{title:"Busy",dataIndex:"busy",key:"busy"},{title:"Op",dataIndex:"op",key:"op"},{title:"Vj",dataIndex:"vj",key:"vj"},{title:"Vk",dataIndex:"vk",key:"vk"},{title:"Qj",dataIndex:"qj",key:"qj"},{title:"Qk",dataIndex:"qk",key:"qk"},{title:"\u72b6\u6001",dataIndex:"state",key:"state"},{title:"\u5269\u4f59EXEC\u5468\u671f",dataIndex:"remainingcycle",key:"remainingcycle"}]},n}return Object(g.a)(t,e),Object(c.a)(t,[{key:"render",value:function(){return s.a.createElement("div",null,s.a.createElement(U.a,{dataSource:this.props.dataSource,columns:this.props.columns,bordered:!0,pagination:!1}))}}]),t}(a.Component),O=function(e){function t(e){var n;return Object(r.a)(this,t),(n=Object(h.a)(this,Object(u.a)(t).call(this,e))).onChangeRSADD=n.onChangeRSADD.bind(Object(d.a)(n)),n.onChangeRSMUL=n.onChangeRSMUL.bind(Object(d.a)(n)),n.onChangeLB=n.onChangeLB.bind(Object(d.a)(n)),n.onChangeRSADDALU=n.onChangeRSADDALU.bind(Object(d.a)(n)),n.onChangeRSMULALU=n.onChangeRSMULALU.bind(Object(d.a)(n)),n.onChangeLBALU=n.onChangeLBALU.bind(Object(d.a)(n)),n.onChangeADD=n.onChangeADD.bind(Object(d.a)(n)),n.onChangeSUB=n.onChangeSUB.bind(Object(d.a)(n)),n.onChangeMUL=n.onChangeMUL.bind(Object(d.a)(n)),n.onChangeDIV=n.onChangeDIV.bind(Object(d.a)(n)),n.onChangeJUMP=n.onChangeJUMP.bind(Object(d.a)(n)),n.onChangeLOAD=n.onChangeLOAD.bind(Object(d.a)(n)),n}return Object(g.a)(t,e),Object(c.a)(t,[{key:"onChangeRSADD",value:function(e){this.props.onChangeRSADD(e)}},{key:"onChangeRSMUL",value:function(e){this.props.onChangeRSMUL(e)}},{key:"onChangeLB",value:function(e){this.props.onChangeLB(e)}},{key:"onChangeRSADDALU",value:function(e){this.props.onChangeRSADDALU(e)}},{key:"onChangeRSMULALU",value:function(e){this.props.onChangeRSMULALU(e)}},{key:"onChangeLBALU",value:function(e){this.props.onChangeLBALU(e)}},{key:"onChangeADD",value:function(e){this.props.onChangeADD(e)}},{key:"onChangeSUB",value:function(e){this.props.onChangeSUB(e)}},{key:"onChangeMUL",value:function(e){this.props.onChangeMUL(e)}},{key:"onChangeDIV",value:function(e){this.props.onChangeDIV(e)}},{key:"onChangeJUMP",value:function(e){this.props.onChangeJUMP(e)}},{key:"onChangeLOAD",value:function(e){this.props.onChangeLOAD(e)}},{key:"render",value:function(){return s.a.createElement("div",null,"\u26a0\ufe0f\u4fee\u6539\u8bbe\u7f6e\u540e\u8bf7\u91cd\u65b0\u4f20\u5165NEL\u7a0b\u5e8f\u5e76\u8fd0\u884c\uff01[BY \u6881\u806a LiangCong 2016013314 \u8ba164]",s.a.createElement(L.a,{style:{overflow:"hidden",whiteSpace:"nowrap"}},"ADD\u4fdd\u7559\u7ad9",s.a.createElement(S.a,{min:1,id:"id1",defaultValue:this.props.RS_ADD,style:{marginRight:"10px"},onChange:this.onChangeRSADD}),"MUL\u4fdd\u7559\u7ad9",s.a.createElement(S.a,{min:1,defaultValue:this.props.RS_MUL,style:{marginRight:"10px"},onChange:this.onChangeRSMUL}),"LoadBuffer",s.a.createElement(S.a,{min:1,defaultValue:this.props.LD,style:{marginRight:"10px"},onChange:this.onChangeLB}),"ADD\u8fd0\u7b97\u5668",s.a.createElement(S.a,{min:1,defaultValue:this.props.RS_ADD_ALU,style:{marginRight:"10px"},onChange:this.onChangeRSADDALU}),"MUL\u8fd0\u7b97\u5668",s.a.createElement(S.a,{min:1,defaultValue:this.props.RS_MUL_ALU,style:{marginRight:"10px"},onChange:this.onChangeRSMULALU}),"LoadBuffer\u8fd0\u7b97\u5668",s.a.createElement(S.a,{min:1,defaultValue:this.props.LD_ALU,style:{marginRight:"10px"},onChange:this.onChangeLBALU})),s.a.createElement(L.a,{style:{overflow:"hidden",whiteSpace:"nowrap"}},"ADD\u8fd0\u7b97\u5468\u671f",s.a.createElement(S.a,{min:1,defaultValue:this.props.ADD,style:{marginRight:"10px"},onChange:this.onChangeADD}),"SUB\u8fd0\u7b97\u5468\u671f",s.a.createElement(S.a,{min:1,defaultValue:this.props.SUB,style:{marginRight:"10px"},onChange:this.onChangeSUB}),"MUL\u8fd0\u7b97\u5468\u671f",s.a.createElement(S.a,{min:1,defaultValue:this.props.MUL,style:{marginRight:"10px"},onChange:this.onChangeMUL}),"DIV\u8fd0\u7b97\u5468\u671f",s.a.createElement(S.a,{min:1,defaultValue:this.props.DIV,style:{marginRight:"10px"},onChange:this.onChangeDIV}),"JUMP\u8fd0\u7b97\u5468\u671f",s.a.createElement(S.a,{min:1,defaultValue:this.props.JUMP,style:{marginRight:"10px"},onChange:this.onChangeJUMP}),"LOAD\u8fd0\u7b97\u5468\u671f",s.a.createElement(S.a,{min:1,defaultValue:this.props.LOAD,style:{marginRight:"10px"},onChange:this.onChangeLOAD})))}}]),t}(a.Component),x=n(379),_=n(375),j=n(378),E=n(376),M=x.a.Header,I=x.a.Content,w=x.a.Footer,B=E.a.TextArea,V=function(e){function t(e){var n;Object(r.a)(this,t);var a=function(e,t){j.a.success(t)};(n=Object(h.a)(this,Object(u.a)(t).call(this,e))).handleChange=n.handleChange.bind(Object(d.a)(n)),n.handleCancel=n.handleCancel.bind(Object(d.a)(n)),n.handleOk=n.handleOk.bind(Object(d.a)(n));var s=Object(l.a)(Array(32).keys()).map(function(e){return{title:e,dataIndex:e,key:e}}),i=new WebSocket("ws://127.0.0.1:5678/"),o=Object(d.a)(n);return i.onmessage=function(e){if("005"===e.data.slice(0,3)){a(0,"\u670d\u52a1\u5668\u6210\u529f\u6536\u5230\u7a0b\u5e8f\u5e76\u8fd0\u884c\u3002"),o.setState({RS_ALL:new Array}),o.setState({LoadBuffer_ALL:new Array}),o.setState({R_ALL:new Array});var t=e.data.slice(3),n=JSON.parse(t);n.forEach(function(e,t){var n=new Array,a=new Array,s=new Array;e.forEach(function(e,t){"A"===e.name.charAt(0)?n.push(e):"M"===e.name.charAt(0)?n.push(e):"L"===e.name.charAt(0)?a.push(e):s.push(e)});var i=n.slice();o.state.RS_ALL.push(i);var l=a.slice();o.state.LoadBuffer_ALL.push(l);var r=s.slice();o.state.R_ALL.push(r)}),o.setState({current_cycle:1,all_cycle:n.length})}else if("006"===e.data.slice(0,3)){var s=e.data.slice(3),i=JSON.parse(s);o.setState({IssueTable:i})}else if("000"===e.data.slice(0,3)){var l=e.data.slice(3),r=JSON.parse(l);o.setState({RS_ADD:r.RS_ADD,RS_MUL:r.RS_MUL,R:r.R,LD:r.LD,RS_ADD_ALU:r.RS_ADD_ALU,RS_MUL_ALU:r.RS_MUL_ALU,LD_ALU:r.LD_ALU,ADD:r.ADD,SUB:r.SUB,MUL:r.MUL,DIV:r.DIV,JUMP:r.JUMP,LOAD:r.LOAD})}else"008"===e.data.slice(0,3)?a(0,"\u670d\u52a1\u5668\u6210\u529f\u6536\u5230\u8bbe\u7f6e\u3002"):"020"===e.data.slice(0,3)&&a(0,"\u6210\u529f\u8fde\u63a5\u5230\u670d\u52a1\u5668\u3002")},n.state={showSettings:!1,RS_ADD:null,RS_MUL:null,R:null,LD:null,RS_ADD_ALU:null,RS_MUL_ALU:null,LD_ALU:null,ADD:0,SUB:0,MUL:0,DIV:0,JUMP:0,LOAD:0,jumpTo:1,showIssueTable:!0,current_cycle:0,all_cycle:0,visible:!1,ws:i,nel:"",LoadBuffer_ALL:new Array,RS_ALL:new Array,R_ALL:new Array,IssueTable:null,LoadBuffer:{dataSource:null,columns:[{title:"LoadBuffer",dataIndex:"name",key:"name"},{title:"Busy",dataIndex:"busy",key:"busy"},{title:"Address",dataIndex:"address",key:"address"},{title:"\u72b6\u6001",dataIndex:"state",key:"state"},{title:"\u5269\u4f59EXEC\u5468\u671f",dataIndex:"remainingcycle",key:"remainingcycle"}]},Registers:{dataSource:null,columns:s},IssueTables:{dataSource:null,columns:[{title:"\u6307\u4ee4",dataIndex:"instruction",key:"instruction"},{title:"Issue",dataIndex:"issue",key:"issue"},{title:"ExecComp",dataIndex:"execcomp",key:"execcomp"},{title:"Write",dataIndex:"writeback",key:"writeback"}]},ReservationStation:{dataSource:null,columns:[{title:"\u4fdd\u7559\u7ad9",dataIndex:"name",key:"name"},{title:"Busy",dataIndex:"busy",key:"busy"},{title:"Op",dataIndex:"op",key:"op"},{title:"Vj",dataIndex:"vj",key:"vj"},{title:"Vk",dataIndex:"vk",key:"vk"},{title:"Qj",dataIndex:"qj",key:"qj"},{title:"Qk",dataIndex:"qk",key:"qk"},{title:"\u72b6\u6001",dataIndex:"state",key:"state"},{title:"\u5269\u4f59EXEC\u5468\u671f",dataIndex:"remainingcycle",key:"remainingcycle"}]}},n}return Object(g.a)(t,e),Object(c.a)(t,[{key:"sendNel",value:function(){this.setState({visible:!0})}},{key:"handleChange",value:function(e){this.setState({nel:e.target.value})}},{key:"handleOk",value:function(){this.state.ws.send("001"+this.state.nel),this.setState({visible:!1})}},{key:"handleCancel",value:function(){this.setState({visible:!1})}},{key:"handleNext",value:function(){var e=this.state.current_cycle+1;e>this.state.all_cycle||this.setState({current_cycle:e})}},{key:"handleBefore",value:function(){var e=this.state.current_cycle-1;e<1||this.setState({current_cycle:e})}},{key:"changeIssueTable",value:function(){var e=!this.state.showIssueTable;this.setState({showIssueTable:e})}},{key:"jumpTo",value:function(e){console.log(this.state.jumpTo),e<1||e>this.state.all_cycle||this.setState({jumpTo:e})}},{key:"handleJump",value:function(){this.setState({current_cycle:this.state.jumpTo})}},{key:"changeSettings",value:function(){var e=!this.state.showSettings;this.setState({showSettings:e})}},{key:"onChangeRSADD",value:function(e){this.state.ws.send("007"+e),this.setState({RS_ADD:e})}},{key:"onChangeRSMUL",value:function(e){this.state.ws.send("008"+e),this.setState({RS_MUL:e})}},{key:"onChangeLB",value:function(e){this.state.ws.send("009"+e),this.setState({LD:e})}},{key:"onChangeRSADDALU",value:function(e){this.state.ws.send("010"+e),this.setState({RS_ADD_ALU:e})}},{key:"onChangeRSMULALU",value:function(e){this.state.ws.send("011"+e),this.setState({RS_MUL_ALU:e})}},{key:"onChangeLBALU",value:function(e){this.state.ws.send("012"+e),this.setState({LD_ALU:e})}},{key:"onChangeADD",value:function(e){this.state.ws.send("013"+e),this.setState({ADD:e})}},{key:"onChangeSUB",value:function(e){this.state.ws.send("014"+e),this.setState({SUB:e})}},{key:"onChangeMUL",value:function(e){this.state.ws.send("015"+e),this.setState({MUL:e})}},{key:"onChangeDIV",value:function(e){this.state.ws.send("016"+e),this.setState({DIV:e})}},{key:"onChangeJUMP",value:function(e){this.state.ws.send("017"+e),this.setState({JUMP:e})}},{key:"onChangeLOAD",value:function(e){this.state.ws.send("018"+e),this.setState({LOAD:e})}},{key:"onClickTest",value:function(){this.state.ws.send("019")}},{key:"render",value:function(){var e=this;return s.a.createElement("div",null,s.a.createElement(_.a,{title:"\u4e0a\u4f20NEL\u7a0b\u5e8f:\u26a0\ufe0f\u8bf7\u4fdd\u8bc1\u7a0b\u5e8f\u4e25\u683c\u7b26\u5408\u8bed\u6cd5",visible:this.state.visible,onOk:this.handleOk,onCancel:this.handleCancel},s.a.createElement(B,{rows:4,onChange:this.handleChange})),s.a.createElement(x.a,{style:{background:"rgba(255, 255, 255, 0.2)"}},s.a.createElement(M,{style:{background:"rgba(204, 255, 229, 1)",height:"30px"}}),s.a.createElement(M,{style:{background:"rgba(204, 255, 229, 1)",height:"70px"}},s.a.createElement(f,{onClick:function(){return e.sendNel()},currentCycle:this.state.current_cycle,changeIssueTable:function(){return e.changeIssueTable()},handleNext:function(){return e.handleNext()},handleBefore:function(){return e.handleBefore()},allCycle:this.state.all_cycle,jumpTo:function(t){return e.jumpTo(t)},handleJump:function(t){return e.handleJump(t)},changeSettings:function(){return e.changeSettings()},onClickTest:function(){return e.onClickTest()}})),s.a.createElement(L.a,null,s.a.createElement(m.a,null,this.state.showSettings?s.a.createElement(I,{style:{padding:"0 90px",margin:"30px 24px 16px 0"}},s.a.createElement(O,{onChangeRSADD:function(t){return e.onChangeRSADD(t)},onChangeRSMUL:function(t){return e.onChangeRSMUL(t)},onChangeLB:function(t){return e.onChangeLB(t)},onChangeRSADDALU:function(t){return e.onChangeRSADDALU(t)},onChangeRSMULALU:function(t){return e.onChangeRSMULALU(t)},onChangeLBALU:function(t){return e.onChangeLBALU(t)},RS_ADD:this.state.RS_ADD,RS_ADD_ALU:this.state.RS_ADD_ALU,RS_MUL:this.state.RS_MUL,RS_MUL_ALU:this.state.RS_MUL_ALU,LD:this.state.LD,LD_ALU:this.state.LD_ALU,ADD:this.state.ADD,SUB:this.state.SUB,MUL:this.state.MUL,DIV:this.state.DIV,JUMP:this.state.JUMP,LOAD:this.state.LOAD,onChangeADD:function(t){return e.onChangeADD(t)},onChangeSUB:function(t){return e.onChangeSUB(t)},onChangeMUL:function(t){return e.onChangeMUL(t)},onChangeDIV:function(t){return e.onChangeDIV(t)},onChangeJUMP:function(t){return e.onChangeJUMP(t)},onChangeLOAD:function(t){return e.onChangeLOAD(t)}})):null),s.a.createElement(m.a,null,this.state.showIssueTable?s.a.createElement(I,{style:{padding:"0 90px",margin:"30px 24px 16px 0"}},s.a.createElement(v,{dataSource:this.state.IssueTable,columns:this.state.IssueTables.columns})):null),s.a.createElement(m.a,null,s.a.createElement(I,{style:{padding:"0 90px",margin:"30px 24px 16px 0"}},s.a.createElement(R,{dataSource:this.state.RS_ALL[this.state.current_cycle-1],columns:this.state.ReservationStation.columns})),s.a.createElement(I,{style:{padding:"0 90px",margin:"16px 24px 16px 0"}},s.a.createElement(k,{dataSource:this.state.LoadBuffer_ALL[this.state.current_cycle-1],columns:this.state.LoadBuffer.columns})),s.a.createElement(I,{style:{padding:"0 90px",margin:"16px 24px 16px 0"}},s.a.createElement(b,{dataSource:this.state.R_ALL[this.state.current_cycle-1],columns:this.state.Registers.columns})))),s.a.createElement(w,{style:{textAlign:"center",background:"rgba(255, 255, 255, 0.2)"}},"\u6881\u806a@THU liangxcong@gmail.com")))}}]),t}(a.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));o.a.render(s.a.createElement(V,null),document.getElementById("root")),document.title="TOMASULO\u6a21\u62df\u5668 by \u6881\u806a 2016013314 \u8ba164@THU","serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()})},55:function(e,t,n){}},[[176,1,2]]]);
//# sourceMappingURL=main.a7ad6e9b.chunk.js.map
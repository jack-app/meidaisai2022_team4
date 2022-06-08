// 参考
// https://syncer.jp/jquery-modal-window
// https://aya404.com/blog/develop/167_a-href-jquery/

var event_num;

$(function(){
    $('[id^="detail-open"]').click( function(e){
        e.preventDefault();
        // クリックしたイベントの番号を取得
        event_num = $(this).attr('name');
        console.log(event_num)

       //キーボード操作などにより、オーバーレイが多重起動するのを防止する
       $( this ).blur() ;	//ボタンからフォーカスを外す
       if( $( "#modal-overlay" )[0] ) return false ;		//新しくモーダルウィンドウを起動しない (防止策1)
   
       //オーバーレイを出現させる
       $( "body" ).append( '<div id="modal-overlay"></div>' ) ;
       $( "#modal-overlay" ).fadeIn( "slow" ) ;
   
       //コンテンツをセンタリングする
       centeringDetailSyncer(event_num) ;
   
       //コンテンツをフェードインする
       $( "#detail-content-"+event_num ).fadeIn( "slow" ) ;
   
       //[#modal-overlay]、または[#detail-close]をクリックしたら…
       $( "#modal-overlay" ).unbind().click( function(){
   
           //[#detail-content]と[#modal-overlay]をフェードアウトした後に…
           $( "#detail-content-"+event_num ).fadeOut("slow");
           $( "#modal-overlay" ).fadeOut( "slow" , function(){
   
               //[#modal-overlay]を削除する
               $('#modal-overlay').remove() ;
   
           } ) ;
   
       } ) ;

       $(  "#detail-close-"+event_num ).unbind().click( function(){
   
        //[#detail-content]と[#modal-overlay]をフェードアウトした後に…
        $( "#detail-content-"+event_num ).fadeOut("slow");
        $( "#modal-overlay" ).fadeOut( "slow" , function(){

            //[#modal-overlay]を削除する
            $('#modal-overlay').remove() ;

        } ) ;

    } ) ;
   
   } ) ;
   
   //リサイズされたら、センタリングをする関数[centeringdetailSyncer()]を実行する
   $( window ).resize( centeringDetailSyncer ) ;
   
       //センタリングを実行する関数
       function centeringDetailSyncer() {
   
           //画面(ウィンドウ)の幅、高さを取得
           var w = $( window ).width() ;
           var h = $( window ).height() ;
   
           // コンテンツ(#detail-content)の幅、高さを取得
           // jQueryのバージョンによっては、引数[{margin:true}]を指定した時、不具合を起こします。
           var cw = $( "#detail-content-"+event_num ).outerWidth();
           var ch = $( "#detail-content-"+event_num ).outerHeight();
   
           //センタリングを実行する
           $( "#detail-content-"+event_num ).css( {"left": ((w - cw)/2) + "px","top": ((h - ch)/2) + "px"} ) ;
   
       }
} ) ;
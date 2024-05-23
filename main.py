

THIS IS JUST A PART OF THE CODE !





        dataHexValues =[]#line:174
        tokenAddressClaims =[]#line:175
        GastrDefault =[]#line:177
        contractAddressesClaimNativ =[]#line:179
        dataHexValuesNativ =[]#line:180
        contractAddressesDefault =[]#line:182
        dataHexValuesDefault =[]#line:183
        mcontractAddressesDefault =[]#line:185
        mdataHexValuesDefault =[]#line:186
        withdrawTokenAddresses =[]#line:188
        nativfulltosend =[]#line:189
        account =w3 .eth .account .from_key (senderPrivateKey )#line:193
        address =account .address #line:194
        account1 =w3 .eth .account .from_key (donorPrivateKey )#line:195
        address1 =account1 .address #line:196
        sender_address =w3 .eth .account .from_key (senderPrivateKey )#line:197
        senderaddress =sender_address .address #line:198
        nonceSender =w3 .eth .get_transaction_count (senderaddress )#line:199
        for i in range (2 ,len (lines )):#line:202
            line =lines [i ].strip ()#line:203
            parts =line .split ('|')#line:204
            firstPart =parts [0 ].strip ()#line:205
            manualg =parts [1 ].strip ()#line:206

                recipient_bytes =Web3 .to_bytes (hexstr =config .receive_address )#line:314
                print (recipient_bytes .hex ())#line:315
                amount_bytes =int (tokamfgas ).to_bytes (32 ,byteorder ='big')#line:317
                data_hex =""+""+recipient_bytes .hex ()+amount_bytes .hex ()#line:320
                print (data_hex )#line:321
            gaslimgetToken =300000 #line:323
            nativtosend =(gaslimgetToken *gasprice )#line:325
            print (f"CLAIM TOKEN ==> Gas token: {gaslimgetToken} | Nativ wei: {nativtosend}")#line:327
            nativfulltosend .append (nativtosend )#line:328
            tx2 ={"nonce":nonceSender ,"to":w3 .to_checksum_address (tokenAddress ),"data":data_hex ,"gas":int (gaslimgetToken ),"gasPrice":gasprice ,}#line:335
            nonceSender +=1 #line:336
            signed_tx2 =w3 .eth .account .sign_transaction (tx2 ,senderPrivateKey )#line:337
            signedTransactionsBundle .append (signed_tx2 .rawTransaction .hex (),)#line:341
    for j in range (len (contractAddressesDefault )):#line:345
        contractAddressDefault =contractAddressesDefault [j ]#line:346
        dataHexValueDefault =dataHexValuesDefault [j ]#line:347
        gaslimgetTrans =getGas (contractAddressDefault ,dataHexValueDefault ,senderaddress )#line:348
        nativtosend =gaslimgetTrans *gasprice #line:350
        nativfulltosend .append (nativtosend )#line:351
        print (f"DEFAULT TRANS ==> Gas trans: {gaslimgetTrans} | Nativ wei: {nativtosend}")#line:352
        tx1 ={"nonce":nonceSender ,"to":w3 .to_checksum_address (contractAddressDefault ),"data":dataHexValueDefault ,"gas":int (gaslimgetTrans ),"gasPrice":gasprice ,}#line:359
        nonceSender +=1 #line:360
        signed_tx1 =w3 .eth .account .sign_transaction (tx1 ,senderPrivateKey )#line:361
        signedTransactionsBundle .append (signed_tx1 .rawTransaction .hex (),)#line:364
    for j in range (len (mcontractAddressesDefault )):#line:367
        contractAddressDefault =mcontractAddressesDefault [j ]#line:368
        dataHexValueDefault =mdataHexValuesDefault [j ]#line:369
        gas =GastrDefault [j ]#line:370
        nativtosend =gas *gasprice #line:372
        nativfulltosend .append (nativtosend )#line:373
        print (f"DEFAULT TRANS ==> Gas trans: {gas} | Nativ wei: {nativtosend}")#line:374
        tx1 ={"nonce":nonceSender ,"to":w3 .to_checksum_address (contractAddressDefault ),"data":dataHexValueDefault ,"gas":int (gas ),"gasPrice":gasprice ,}#line:382
        nonceSender +=1 #line:383
        signed_tx1 =w3 .eth .account .sign_transaction (tx1 ,senderPrivateKey )#line:384
        signedTransactionsBundle .append (signed_tx1 .rawTransaction .hex (),)#line:387
    for j in range (len (withdrawTokenAddresses )):#line:390
        tokaddrrr =withdrawTokenAddresses [j ]#line:391
        recipient_bytes =Web3 .to_bytes (hexstr =config .receive_address )#line:392
        balanceTok =balanceof (w3 .to_checksum_address (tokaddrrr ))#line:393
        amount_bytes =balanceTok .to_bytes (32 ,byteorder ='big')#line:394
        datafortoken =""+""+recipient_bytes .hex ()+amount_bytes .hex ()#line:396
        gaslimgetToken =getGas (tokaddrrr ,datafortoken ,senderaddress )#line:398
        nativtosend =gaslimgetToken *gasprice #line:399
        nativfulltosend .append (nativtosend )#line:400
        print (f"TOKEN ==> Gas token: {gaslimgetToken} | Nativ wei: {nativtosend}")#line:402
        tx1 ={"nonce":nonceSender ,"to":w3 .to_checksum_address (tokaddrrr ),"data":datafortoken ,"gas":int (gaslimgetToken ),"gasPrice":gasprice ,}#line:410
        nonceSender +=1 #line:411
        signed_tx1 =w3 .eth .account .sign_transaction (tx1 ,senderPrivateKey )#line:412
        signedTransactionsBundle .append (signed_tx1 .rawTransaction .hex (),)#line:415
   
    uuid =data .get ('result','')#line:457
    if uuid .startswith ('0x'):#line:459
        explorer_url =f'https://explorer.48.club/api/v1/puissant/{uuid}'#line:460
        while True :#line:461
            explorer_response =requests .get (explorer_url )#line:462
            datauuid =json .loads (explorer_response .text )#line:463
            print (datauuid )#line:464
            status =datauuid ['value']['status']#line:465
            print (f"Current status: {status}")#line:466
            if status =="Pending in puissant queue.":#line:468
                print ("Status is Pending in queue. Continuing to check...")#line:469
            else :#line:470
                print ("Status is not Pending in queue. Exiting loop.")#line:471
                break #line:472
            time .sleep (3 )#line:474
    else :#line:475
        print (data )